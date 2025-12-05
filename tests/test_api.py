import os
import sys
from pathlib import Path

# On ajoute le dossier RACINE du projet au PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from src.app.main import app   # <--- IMPORTANT : src.app.main

from fastapi.testclient import TestClient

client = TestClient(app)



def _valid_payload(**overrides):
    base = {
        "age": 30,
        "annee_experience_totale": 5,
        "revenu_mensuel": 2500.0,
        "distance_domicile_travail": 10.0,
        "nb_formations_suivies": 2,
        "nombre_heures_travaillees": 40.0,
        "frequence_deplacement": "Rarement",
    }
    base.update(overrides)
    return base

    


def test_predict_ok():
    payload = _valid_payload()
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1]


def test_predict_missing_field():
    payload = _valid_payload()
    payload.pop("revenu_mensuel")
    r = client.post("/predict", json=payload)
    assert r.status_code == 422


