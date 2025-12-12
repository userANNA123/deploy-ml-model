from pydantic import BaseModel, Field
from typing import Literal, Optional


class PredictionRequest(BaseModel):
    age: int = Field(..., ge=16, le=80)
    annee_experience_totale: int = Field(..., ge=0, le=60)
    revenu_mensuel: float = Field(..., ge=0)
    distance_domicile_travail: float = Field(..., ge=0)
    nb_formations_suivies: int = Field(..., ge=0)
    nombre_heures_travaillees: float = Field(..., ge=0)
    frequence_deplacement: Literal["Jamais", "Rarement", "Souvent"]

    from pydantic import BaseModel, ConfigDict

class PredictionRequest(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "age": 30,
                "annee_experience_totale": 5,
                "revenu_mensuel": 3000,
                "distance_domicile_travail": 10,
                "nb_formations_suivies": 2,
                "nombre_heures_travaillees": 160,
                "frequence_deplacement": "Rarement"
            }
        }
    )
    # ... fields


class PredictionResponse(BaseModel):
    prediction: int  # 0 = reste, 1 = churn 

