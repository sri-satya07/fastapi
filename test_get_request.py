import pytest
from fastapi.testclient import TestClient
from main import app  


client = TestClient(app)
@pytest.mark.order(1)
def test_get_users():
    response = client.get("/api/hello/")
    assert response.status_code == 200     
    print("helloowwwww")

@pytest.mark.order(2)  
def test_get_user():
    response = client.get("/api/users/")
    assert response.status_code == 200
    users = response.json()
    print(users)


@pytest.mark.order(3)
def test_create_users():
    body = {
    "name": "sai",
    "email": "sai@gmail.com",
    "password": "sai@123"
}
   
    response = client.post("/api/users/create/", json=body)
    assert response.status_code == 200
    
