"""Unit tests for SECClient class"""

import pytest
from app.services.sec_client import SECClient

@pytest.fixture
def sec_client():
    return SECClient(email="test@example.com")

def test_get_latest_10k_url_returns_correct_url(monkeypatch, sec_client):
    """Mock SEC JSON response and verify URL formation"""
    
    class MockResponse:
        def raise_for_status(self): pass
        def json(self):
            return {
                "filings": {
                    "recent": {
                        "form": ["10-K", "10-Q"],
                        "accessionNumber": ["0000000000-21-000001", "0000000000-21-000002"],
                        "primaryDocument": ["test10k.htm", "test10q.htm"]
                    }
                }
            }

    # Patch requests.get to return the mock response
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse())
    
    url = sec_client.get_latest_10k_url("0000000000")
    assert url.startswith("https://www.sec.gov/Archives/edgar/data/0000000000/")
    assert url.endswith("test10k.htm")

def test_get_latest_10k_url_no_10k(monkeypatch, sec_client):
    """Return None if no 10-K filing is found"""
    
    class MockResponseNo10K:
        def raise_for_status(self): pass
        def json(self):
            return {
                "filings": {
                    "recent": {
                        "form": ["10-Q"],
                        "accessionNumber": ["0000000000-21-000002"],
                        "primaryDocument": ["test10q.htm"]
                    }
                }
            }

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponseNo10K())
    url = sec_client.get_latest_10k_url("0000000000")
    assert url is None