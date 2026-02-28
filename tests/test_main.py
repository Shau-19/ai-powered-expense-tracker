from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat):
    response = client.post("/chat", json={"message": "Hello World"})
    assert response.status_code == 200
    assert response.json()["message"] == "Hello World"

def test_create_expense():
    response = client.post("/expenses", json={"amount": 10.99, "description": "Lunch"})
    assert response.status_code == 200
    assert "amount" in response.json()
    assert "description" in response.json()
    assert "category" in response.json()