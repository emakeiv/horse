from fastapi import APIRouter

from src.api.v1.schemas.router import RouteRequest, RouteResponse

router = APIRouter(
    prefix="/router",
    tags=["router"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=RouteResponse)
async def route(req: RouteRequest) -> RouteResponse:
    pass