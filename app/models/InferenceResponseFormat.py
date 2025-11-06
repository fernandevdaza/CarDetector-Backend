from pydantic import BaseModel, Field

class InferenceResponseFormat(BaseModel):
    brand: str = Field()
    model_name: str = Field()
    year: int = Field()
    lat: float = Field()
    lng: float = Field()