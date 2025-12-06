import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from src.app.main import app


client = TestClient(app)


def _valid_payload(**overrides):
    base = {
        "age": 30,
        "annee_experience_totale": 5,
        "revenu_mensuel": 3000.0,
        "distance_domicile_travail": 12.5,
        "nb_formations_suivies": 2,
        "nombre_heures_travaillees": 160.0,
        "frequence_deplacement": "Rarement",
    }
    base.update(overrides)
    return base


def test_predict_ok():
    r = client.post("/predict", json=_valid_payload())
    assert r.status_code == 200
    assert "prediction" in r.json()


def test_predict_missing_field():
    data = _valid_payload()
    data.pop("revenu_mensuel")
    r = client.post("/predict", json=data)
    assert r.status_code == 422
