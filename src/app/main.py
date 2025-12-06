from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import json

from .schemas import PredictionRequest, PredictionResponse
from .ml_model import predict_from_dict
from .db import SessionLocal
from .models import ModelInput, ModelOutput  

app = FastAPI(
    title="Churn Prediction API",
    description="API pour exposer le modèle RandomForest du projet 4",
    version="1.0.0",
)


# Dependency pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(
    payload: PredictionRequest,
    db: Session = Depends(get_db),
):
    try:
        # 1) convertir le payload Pydantic en dict
        data = payload.model_dump()

        # 2) enregistrer l'input dans la base
        input_row = ModelInput(payload=json.dumps(data, ensure_ascii=False))
        db.add(input_row)
        db.commit()
        db.refresh(input_row)

        # 3) appeler le modèle
        result = predict_from_dict(data)

        # 4) enregistrer l'output dans la base
        output_row = ModelOutput(
            input_id=input_row.id,
            prediction=result,
        )
        db.add(output_row)
        db.commit()

        # 5) retourner la réponse API
        return PredictionResponse(prediction=result)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


