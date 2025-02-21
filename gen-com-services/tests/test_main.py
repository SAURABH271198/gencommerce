from fastapi.testclient import TestClient
from src.main import app  # Adjust the import if your app entry point is different

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to GenCommerce Backend"}


def test_invalid_route():
    response = client.get("/invalid-route")
    assert response.status_code == 404
