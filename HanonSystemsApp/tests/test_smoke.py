# tests/test_smoke.py
import pytest
from django.apps import apps
from django.db import connections


def test_apps_loaded():
    assert apps.is_installed("database")
    assert apps.is_installed("members")


@pytest.mark.django_db(transaction=True)
def test_db_connection():
    with connections["default"].cursor() as cur:
        cur.execute("SELECT 1")
        row = cur.fetchone()
    assert row[0] == 1
