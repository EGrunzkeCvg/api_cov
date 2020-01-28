import pytest
from starlette.testclient import TestClient
from api_cov.app import app


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    return client
