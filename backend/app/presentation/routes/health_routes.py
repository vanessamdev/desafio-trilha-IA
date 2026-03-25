"""
Health Check Routes
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Check API health status"""
    pass
