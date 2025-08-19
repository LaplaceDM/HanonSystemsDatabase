# tests/test_smoke.py
import pytest
from django.apps import apps
from django.db import connections

def test_apps_loaded():
    # 验证关键 app 是否正确安装（按你的 settings.py）
    assert apps.is_installed("database")
    assert apps.is_installed("members")

@pytest.mark.django_db(transaction=True)
def test_db_connection():
    # 简单连一下数据库，验证 ODBC/MS SQL 配置无误
    with connections["default"].cursor() as cur:
        cur.execute("SELECT 1")
        row = cur.fetchone()
    assert row[0] == 1
