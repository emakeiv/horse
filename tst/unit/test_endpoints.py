from fastapi.testclient import TestClient
from src.api.v1.server import create_app

client = TestClient(create_app())

def test_health_ok():
    response = client.get("/api/v1/health")
    assert response.status_code == 200

