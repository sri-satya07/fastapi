import pytest
from fastapi.testclient import TestClient
from typing import List
from main import app  # Import your FastAPI app

client = TestClient(app)
@pytest.mark.order(1)
def test_get_users():
    response = client.get("/api/hello/")
    assert response.status_code == 200
     
    print("helloowwwww")
