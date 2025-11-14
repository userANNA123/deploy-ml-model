from fastapi import FastAPI, HTTPException
from .schemas import PredictionRequest, PredictionResponse
from .ml_model import predict

app = FastAPI(
    title="ML Prediction API",
    description="API pour exposer un modèle de machine learning",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(payload: PredictionRequest):
    try:
        result = predict(
            surface=payload.surface,
            nb_rooms=payload.nb_rooms,
            year_built=payload.year_built
        )
        return PredictionResponse(prediction=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
