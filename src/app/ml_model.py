from pathlib import Path
import joblib
import pandas as pd
import numpy as np

FREQ_NUM_MAP = {"Jamais": 0, "Rarement": 1, "Souvent": 2}

MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "churn_model.joblib"
_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    هذه نسخة مبسّطة من make_features الموجودة في الـ notebook.
    عدّليها لتطابق الكود الأصلي قدر الإمكان.
    """

    df2 = df.copy()

    # 1) expérience_to_age
    if "annee_experience_totale" in df2.columns and "age" in df2.columns:
        df2["experience_to_age"] = (
            df2["annee_experience_totale"] / df2["age"].replace(0, np.nan)
        ).replace([np.inf, -np.inf], np.nan)

    # 2) salary_category par quartiles
    if "revenu_mensuel" in df2.columns:
        try:
            df2["salary_category"] = pd.qcut(
                df2["revenu_mensuel"],
                q=4,
                labels=["low", "medium", "high", "very_high"],
            )
        except ValueError:
            # fallback لو البيانات قليلة
            df2["salary_category"] = pd.cut(
                df2["revenu_mensuel"],
                bins=4,
                labels=["low", "medium", "high", "very_high"],
                include_lowest=True,
            )

    # 3) trajets longs
    if "distance_domicile_travail" in df2.columns:
        med_dist = df2["distance_domicile_travail"].median()
        df2["long_commute"] = (df2["distance_domicile_travail"] > med_dist).astype(int)

    # 4) training_hours_per_year
    if "nb_formations_suivies" in df2.columns:
        df2["training_hours_per_year"] = df2["nb_formations_suivies"].fillna(0) * 8

    # 5) work_life_balance index basé sur frequence_deplacement + nombre_heures_travaillees
    if (
        "frequence_deplacement" in df2.columns
        and "nombre_heures_travaillees" in df2.columns
    ):
        freq_code = (
            df2["frequence_deplacement"]
            .map(FREQ_NUM_MAP)
            .fillna(0)
        )
        df2["work_life_balance"] = (
            df2["nombre_heures_travaillees"] / (freq_code + 1)
        )

    # TODO: لو في الـ notebook كود إضافي (drop بعض الأعمدة أو إنشاء أعمدة أخرى)
    # انسخيه هنا.

    return df2

# TODO: عدّلي هذه القائمة لتطابق الأعمدة التي استخدمتها في X_train في مشروع 4
X_COLUMNS = [
    "age",
    "annee_experience_totale",
    "revenu_mensuel",
    "distance_domicile_travail",
    "nb_formations_suivies",
    "nombre_heures_travaillees",
    "experience_to_age",
    "salary_category",
    "long_commute",
    "training_hours_per_year",
    "work_life_balance",
]

def predict_from_dict(data: dict) -> int:
    """
    data: dict venant من Pydantic (PredictionRequest.dict())
    retourne 0 ou 1 selon le modèle rf.
    """
    model = load_model()

    # 1) construire DataFrame à partir des données
    df = pd.DataFrame([data])

    # 2) appliquer les mêmes features que dans le notebook
    df_feat = make_features(df)

    # 3) s'assurer qu'on a exactement les colonnes X_COLUMNS
    X = df_feat[X_COLUMNS]

    y_pred = model.predict(X)
    return int(y_pred[0])


