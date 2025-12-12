import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from src.app.main import app
import pytest
from httpx import AsyncClient, ASGITransport
from src.app.main import app

@pytest.mark.asyncio
async def test_predict():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/predict", json={
            "age": 30,
            "annee_experience_totale": 5,
            "revenu_mensuel": 3000,
            "distance_domicile_travail": 10,
            "nb_formations_suivies": 2,
            "nombre_heures_travaillees": 160,
            "frequence_deplacement": "Rarement"
        })
    assert r.status_code == 200
    assert "prediction" in r.json()
