import fakeredis
import pytest
from fastapi.testclient import TestClient

from app import main


@pytest.fixture(autouse=True)
def faux_redis(monkeypatch):
    monkeypatch.setattr(main, "r", fakeredis.FakeRedis(decode_responses=True))


client = TestClient(main.app)


def test_root_incremente_le_compteur():
    assert client.get("/").json() == {"visites": 1}
    assert client.get("/").json() == {"visites": 2}


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_metrics():
    assert client.get("/metrics").status_code == 200
