"""
Image Processing Routes
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/detect-labels")
async def detect_labels():
    """Detect labels in image using AWS Rekognition"""
    return {"message": "Use /analyze-contract endpoint"}


@router.post("/detect-faces")
async def detect_faces():
    """Detect faces in image"""
    return {"message": "Use /analyze-contract endpoint"}
