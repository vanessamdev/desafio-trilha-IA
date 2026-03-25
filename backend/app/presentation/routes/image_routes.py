"""
Image Processing Routes
"""
from fastapi import APIRouter, Depends, UploadFile, File

from backend.app.core.dependencies import get_image_recognition_use_case
from backend.app.application.use_cases.image_recognition_use_case import ImageRecognitionUseCase

router = APIRouter()


@router.post("/detect-labels")
async def detect_labels(
    file: UploadFile = File(...),
    use_case: ImageRecognitionUseCase = Depends(get_image_recognition_use_case)
):
    """Detect labels in image using AWS Rekognition"""
    pass


@router.post("/detect-faces")
async def detect_faces(
    file: UploadFile = File(...),
    use_case: ImageRecognitionUseCase = Depends(get_image_recognition_use_case)
):
    """Detect faces in image"""
    pass
