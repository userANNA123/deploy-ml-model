from fastapi import FastAPI, HTTPException
from .schemas import PredictionRequest, PredictionResponse
from .ml_model import predict_from_dict

app = FastAPI(
    title="Churn Prediction API",
    description="API pour exposer le modèle RandomForest du projet 4",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(payload: PredictionRequest):
    try:
        data = payload.dict()
        result = predict_from_dict(data)
        return PredictionResponse(prediction=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

