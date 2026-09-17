from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "YuvOps API is running"
    assert data["status"] == "ok"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }

def test_api_status():
    response = client.get("/api/v1/status")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "YuvOps API"
    assert data["version"] == "v1"
    assert data["status"] == "operational"

def test_api_info():
    response = client.get("/api/v1/info")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "YuvOps API"
    assert data["version"] == "1.0.0"
    assert data["environment"] == "development"