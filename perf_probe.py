#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Performance probe for web endpoints (HTTP) and SQL Server (pyodbc).
- Output data fields are in English.
- Explanations and comments are in Chinese for easier operation.

Usage examples:
  # 仅测 HTTP, 多端点, 多次重复，并发 5, 导出 JSON/CSV
  python perf_probe.py \
    --base-url http://127.0.0.1:8000 \
    --endpoints / /product /tests \
    --runs 5 --concurrency 5 \
    --json-out web.json --csv-out web.csv

  # 加测浏览器级页面性能（需安装 playwright)
  python perf_probe.py \
    --base-url http://127.0.0.1:8000 \
    --browser-endpoints / /product \
    --browser-timeout 30 \
    --json-out browser.json

  # 测数据库连接与查询
  python perf_probe.py \
    --db-conn "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost,1433;DATABASE=hanonsystems_database;UID=sa;PWD=Password123;TrustServerCertificate=yes" \
    --db-queries "SELECT 1" "SELECT COUNT(*) FROM database_product" \
    --json-out db.json --csv-out db.csv
"""

import argparse
import csv
import json
import math
import os
import platform
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from time import perf_counter
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin

# 可选依赖按需导入（未安装也能跑 HTTP/DB 部分）
try:
    import requests
except Exception as e:  # pragma: no cover
    print("ERROR: The 'requests' package is required.", file=sys.stderr)
    raise

try:
    import pyodbc
except Exception:
    pyodbc = None  # 没装也允许，仅禁用 DB 测试

# Playwright 可选
try:
    from playwright.sync_api import sync_playwright
except Exception:
    sync_playwright = None


# -----------------------------
# 工具函数
# -----------------------------
def percentile(data: List[float], p: float) -> float:
    """计算百分位, data 单位为毫秒"""
    if not data:
        return float("nan")
    k = (len(data) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    return data[f] + (data[c] - data[f]) * (k - f)


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())


# -----------------------------
# HTTP 测试
# -----------------------------
@dataclass
class HttpSample:
    endpoint: str
    status_code: int
    ttfb_ms: float
    total_ms: float
    content_bytes: int
    ok: bool
    started_at: str

def measure_http_once(session: requests.Session, full_url: str, timeout: float) -> HttpSample:
    """
    用 requests 测 TTFB 与总耗时：
      - TTFB: 从发起请求到收到首个字节（通过 stream + iter_content)
      - total_ms: 下载完整响应体的耗时
    """
    started = now_iso()
    start = perf_counter()
    content_len = 0
    status = 0
    ok = False
    ttfb_ms = float("nan")
    try:
        with session.get(full_url, timeout=timeout, stream=True) as resp:
            status = resp.status_code
            # 首字节时间：拉一小块内容
            first_chunk_start = perf_counter()
            for chunk in resp.iter_content(chunk_size=4096):
                ttfb_ms = (perf_counter() - start) * 1000.0
                if chunk:
                    content_len += len(chunk)
                    break
            # 继续读完剩余内容
            for chunk in resp.iter_content(chunk_size=65536):
                if chunk:
                    content_len += len(chunk)
            ok = 200 <= status < 400
    except Exception:
        ttfb_ms = float("nan")
        ok = False
    total_ms = (perf_counter() - start) * 1000.0
    return HttpSample(
        endpoint=full_url,
        status_code=status,
        ttfb_ms=ttfb_ms,
        total_ms=total_ms,
        content_bytes=content_len,
        ok=ok,
        started_at=started,
    )


def run_http_probes(
    base_url: str,
    endpoints: List[str],
    runs: int,
    concurrency: int,
    timeout: float,
) -> List[HttpSample]:
    """
    多端点 * 多次重复 * 并发 方式测试。
    """
    samples: List[HttpSample] = []
    work: List[Tuple[str, int]] = []  # (full_url, run_index)
    with requests.Session() as session:
        session.headers.update({"User-Agent": "perf-probe/1.0"})
        for ep in endpoints:
            full = urljoin(base_url.rstrip("/") + "/", ep.lstrip("/"))
            for i in range(runs):
                work.append((full, i))

        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = [pool.submit(measure_http_once, session, url, timeout) for (url, _) in work]
            for fut in as_completed(futures):
                samples.append(fut.result())
    return samples


# -----------------------------
# 浏览器（Playwright）页面测量（可选）
# -----------------------------
@dataclass
class BrowserSample:
    endpoint: str
    ttfb_ms: float
    dom_content_loaded_ms: float
    load_event_ms: float
    started_at: str
    ok: bool
    status_code: Optional[int]

def run_browser_probes(base_url: str, endpoints: List[str], timeout: float) -> List[BrowserSample]:
    if sync_playwright is None:
        print("WARN: Playwright not installed; browser tests skipped.", file=sys.stderr)
        return []

    results: List[BrowserSample] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for ep in endpoints:
            url = urljoin(base_url.rstrip("/") + "/", ep.lstrip("/"))
            started = now_iso()
            ok = False
            status_code = None
            ttfb_ms = float("nan")
            dcl_ms = float("nan")
            load_ms = float("nan")
            try:
                # 记录响应码（主文档）
                def _route_response(resp):
                    nonlocal status_code
                    if resp.url == url and status_code is None:
                        status_code = resp.status

                page.on("response", _route_response)
                nav_resp = page.goto(url, wait_until="load", timeout=int(timeout * 1000))
                # 计算 Navigation Timing
                timing = page.evaluate(
                    """() => {
                        const [nav] = performance.getEntriesByType('navigation');
                        if (!nav) return null;
                        return {
                          ttfb: nav.responseStart - nav.startTime,
                          dcl: nav.domContentLoadedEventEnd - nav.startTime,
                          load: nav.loadEventEnd - nav.startTime
                        };
                    }"""
                )
                if timing:
                    ttfb_ms = float(timing["ttfb"])
                    dcl_ms = float(timing["dcl"])
                    load_ms = float(timing["load"])
                ok = True
            except Exception:
                ok = False
            finally:
                results.append(
                    BrowserSample(
                        endpoint=url,
                        ttfb_ms=ttfb_ms,
                        dom_content_loaded_ms=dcl_ms,
                        load_event_ms=load_ms,
                        started_at=started,
                        ok=ok,
                        status_code=status_code,
                    )
                )
        browser.close()
    return results


# -----------------------------
# 数据库测量（SQL Server）
# -----------------------------
@dataclass
class DbSample:
    action: str  # "connect" or "query"
    target: str  # DSN for connect; query text for query
    elapsed_ms: float
    ok: bool
    rows: Optional[int]
    started_at: str
    error: Optional[str]

def run_db_probes(conn_str: str, queries: List[str], timeout: float) -> List[DbSample]:
    results: List[DbSample] = []
    if pyodbc is None:
        print("WARN: pyodbc not installed; DB tests skipped.", file=sys.stderr)
        return results

    # 连接时间
    started = now_iso()
    t0 = perf_counter()
    cnx = None
    try:
        # 注：pyodbc 自身不支持超时的连接参数；部分驱动可用 Connection Timeout
        cnx = pyodbc.connect(conn_str, autocommit=True, timeout=int(timeout))
        ok = True
        err = None
    except Exception as e:
        ok = False
        err = str(e)
    elapsed = (perf_counter() - t0) * 1000.0
    results.append(
        DbSample(
            action="connect",
            target="dsn",
            elapsed_ms=elapsed,
            ok=ok,
            rows=None,
            started_at=started,
            error=err,
        )
    )
    if not ok or cnx is None:
        return results

    # 查询时间
    try:
        cur = cnx.cursor()
        for q in queries:
            started = now_iso()
            t0 = perf_counter()
            rows = None
            q_ok = False
            q_err = None
            try:
                cur.execute(q)
                try:
                    data = cur.fetchall()
                    rows = len(data)
                except pyodbc.ProgrammingError:
                    rows = 0  # 非查询语句
                q_ok = True
            except Exception as e:
                q_err = str(e)
                q_ok = False
            elapsed = (perf_counter() - t0) * 1000.0
            results.append(
                DbSample(
                    action="query",
                    target=q,
                    elapsed_ms=elapsed,
                    ok=q_ok,
                    rows=rows,
                    started_at=started,
                    error=q_err,
                )
            )
    finally:
        try:
            cnx.close()
        except Exception:
            pass
    return results


# -----------------------------
# 汇总与导出
# -----------------------------
def summarize_http(samples: List[HttpSample]) -> Dict:
    by_ep: Dict[str, List[HttpSample]] = {}
    for s in samples:
        by_ep.setdefault(s.endpoint, []).append(s)

    summary = {"kind": "http_summary", "generated_at": now_iso(), "endpoints": []}
    for ep, arr in by_ep.items():
        total_ms = sorted([x.total_ms for x in arr if x.total_ms == x.total_ms])
        ttfb_ms = sorted([x.ttfb_ms for x in arr if x.ttfb_ms == x.ttfb_ms])
        ok_rate = sum(1 for x in arr if x.ok) / len(arr)
        sizes = [x.content_bytes for x in arr]
        item = {
            "endpoint": ep,
            "runs": len(arr),
            "ok_rate": round(ok_rate, 4),
            "status_codes": sorted({x.status_code for x in arr}),
            "bytes_avg": int(statistics.mean(sizes)) if sizes else 0,
            "ttfb_ms_avg": round(statistics.mean(ttfb_ms), 2) if ttfb_ms else None,
            "ttfb_ms_p95": round(percentile(ttfb_ms, 95), 2) if ttfb_ms else None,
            "total_ms_avg": round(statistics.mean(total_ms), 2) if total_ms else None,
            "total_ms_p95": round(percentile(total_ms, 95), 2) if total_ms else None,
        }
        summary["endpoints"].append(item)
    summary["system"] = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
    }
    return summary


def write_json(path: str, payload) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_csv(path: str, rows: List[Dict[str, object]], fieldnames: List[str]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


# -----------------------------
# CLI
# -----------------------------
def main():
    p = argparse.ArgumentParser(description="Web & DB performance probe")
    # HTTP
    p.add_argument("--base-url", help="Base URL, e.g. http://127.0.0.1:8000")
    p.add_argument("--endpoints", nargs="*", default=[], help="HTTP endpoints to test")
    p.add_argument("--runs", type=int, default=3, help="Repeat count per endpoint (HTTP)")
    p.add_argument("--concurrency", type=int, default=4, help="Concurrent workers (HTTP)")
    p.add_argument("--http-timeout", type=float, default=20.0, help="HTTP timeout (seconds)")

    # Browser
    p.add_argument("--browser-endpoints", nargs="*", default=[], help="Endpoints to test in a real browser")
    p.add_argument("--browser-timeout", type=float, default=30.0, help="Browser nav timeout (seconds)")

    # DB
    p.add_argument("--db-conn", default=None, help="pyodbc connection string for SQL Server")
    p.add_argument("--db-queries", nargs="*", default=[], help="SQL queries to measure")
    p.add_argument("--db-timeout", type=float, default=15.0, help="DB connect/query timeout (seconds)")

    # Output
    p.add_argument("--json-out", default=None, help="Write all results to JSON")
    p.add_argument("--csv-out", default=None, help="Write flat CSV (mixed kinds)")

    args = p.parse_args()

    all_out_rows: List[Dict[str, object]] = []
    json_bundle: Dict[str, object] = {
        "generated_at": now_iso(),
        "host": platform.node(),
        "python": sys.version.split()[0],
        "results": {},
    }

    # HTTP
    if args.base_url and args.endpoints:
        http_samples = run_http_probes(
            base_url=args.base_url,
            endpoints=args.endpoints,
            runs=args.runs,
            concurrency=args.concurrency,
            timeout=args.http-timeout if hasattr(args, "http-timeout") else args.http_timeout,
        )
        http_summary = summarize_http(http_samples)
        json_bundle["results"]["http_samples"] = [asdict(x) for x in http_samples]
        json_bundle["results"]["http_summary"] = http_summary
        # 追加到 CSV 扁平表
        for s in http_samples:
            all_out_rows.append(
                {
                    "kind": "http",
                    "endpoint": s.endpoint,
                    "status_code": s.status_code,
                    "ttfb_ms": round(s.ttfb_ms, 2) if s.ttfb_ms == s.ttfb_ms else "",
                    "total_ms": round(s.total_ms, 2),
                    "content_bytes": s.content_bytes,
                    "ok": int(bool(s.ok)),
                    "started_at": s.started_at,
                }
            )

    # Browser
    if args.base_url and args.browser_endpoints:
        browser_results = run_browser_probes(
            base_url=args.base_url,
            endpoints=args.browser_endpoints,
            timeout=args.browser_timeout,
        )
        json_bundle["results"]["browser_samples"] = [asdict(x) for x in browser_results]
        for b in browser_results:
            all_out_rows.append(
                {
                    "kind": "browser",
                    "endpoint": b.endpoint,
                    "status_code": b.status_code if b.status_code is not None else "",
                    "ttfb_ms": round(b.ttfb_ms, 2) if b.ttfb_ms == b.ttfb_ms else "",
                    "dom_content_loaded_ms": round(b.dom_content_loaded_ms, 2)
                    if b.dom_content_loaded_ms == b.dom_content_loaded_ms
                    else "",
                    "load_event_ms": round(b.load_event_ms, 2) if b.load_event_ms == b.load_event_ms else "",
                    "ok": int(bool(b.ok)),
                    "started_at": b.started_at,
                }
            )

    # DB
    if args.db_conn:
        db_results = run_db_probes(args.db_conn, args.db_queries, timeout=args.db_timeout)
        json_bundle["results"]["db_samples"] = [asdict(x) for x in db_results]
        for d in db_results:
            all_out_rows.append(
                {
                    "kind": f"db_{d.action}",
                    "target": d.target,
                    "elapsed_ms": round(d.elapsed_ms, 2),
                    "ok": int(bool(d.ok)),
                    "rows": d.rows if d.rows is not None else "",
                    "error": d.error if d.error else "",
                    "started_at": d.started_at,
                }
            )

    # 输出
    if args.json_out:
        write_json(args.json_out, json_bundle)
        print(f"[OK] JSON written: {args.json_out}")
    if args.csv_out and all_out_rows:
        # 统一字段（缺省的留空）
        fieldnames = sorted({k for r in all_out_rows for k in r.keys()})
        write_csv(args.csv_out, all_out_rows, fieldnames=fieldnames)
        print(f"[OK] CSV written: {args.csv_out}")

    # 控制台简报（英文字段，便于复制到 wiki/issue）
    print("\n=== quick summary (english fields) ===")
    for r in all_out_rows:
        print(r)
    print(f"total rows: {len(all_out_rows)}")


if __name__ == "__main__":
    main()
