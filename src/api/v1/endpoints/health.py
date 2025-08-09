from fastapi import APIRouter, status

from src.api.v1.schemas.health import HealthCheckResponse

router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', response_model= HealthCheckResponse, status_code=status.HTTP_200_OK)
async def health() -> HealthCheckResponse: # noqa: D401
    return HealthCheckResponse()