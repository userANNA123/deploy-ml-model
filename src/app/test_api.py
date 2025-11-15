from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict():
    r = client.post("/predict", json={
        "surface": 40,
        "nb_rooms": 2,
        "year_built": 2000
    })
    assert r.status_code == 200
    assert "prediction" in r.json()
