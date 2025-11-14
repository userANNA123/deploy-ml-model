from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    surface: float = Field(..., gt=0, description="Surface en m²")
    nb_rooms: int = Field(..., ge=0, description="Nombre de pièces")
    year_built: int = Field(..., ge=1800, le=2100, description="Année de construction")

class PredictionResponse(BaseModel):
    prediction: float
