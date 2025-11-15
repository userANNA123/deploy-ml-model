# src/app/ml_model.py

def predict(surface: float, nb_rooms: int, year_built: int) -> float:
    """
    Dummy prediction (temporaire).
    Remplacer plus tard par:
        - chargement du modèle via joblib
        - préprocessing
        - modèle.predict(...)
    """
    return surface * 10  # Simule une prédiction

