from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    response2 = client.get("/item/35")
    assert  response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    assert response2.json() == {"item_id": 35}