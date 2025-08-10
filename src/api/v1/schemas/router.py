from pydantic import BaseModel, Field

class RouteRequest(BaseModel):
    prompt: str = Field()

class RouteResponse(BaseModel):
    model: str
    reasons: list[str]
    features: dict