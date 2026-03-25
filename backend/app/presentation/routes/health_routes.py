"""
Health Check Routes
"""
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from backend.app.core.config import Settings
from backend.app.core.dependencies import get_config


router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check(config: Settings = Depends(get_config)) -> HealthResponse:
    """Check API health status"""
    return HealthResponse(
        status="healthy",
        app_name=config.APP_NAME,
        version=config.APP_VERSION
    )
