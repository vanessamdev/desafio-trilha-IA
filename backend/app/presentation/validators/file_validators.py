"""
File Upload Validators
"""
from fastapi import UploadFile, HTTPException, status

ALLOWED_DOCUMENT_TYPES = [
    "application/pdf",
    "image/png",
    "image/jpeg",
    "image/jpg"
]

ALLOWED_IMAGE_TYPES = [
    "image/png",
    "image/jpeg",
    "image/jpg"
]

MAX_DOCUMENT_SIZE = 10 * 1024 * 1024  # 10MB
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB


async def validate_document(file: UploadFile) -> bytes:
    """Validate document file type and size"""
    if file.content_type not in ALLOWED_DOCUMENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid document type. Allowed: PDF, PNG, JPEG"
        )
    
    content = await file.read()
    
    if len(content) > MAX_DOCUMENT_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Document too large. Max size: 10MB"
        )
    
    return content


async def validate_face_image(file: UploadFile) -> bytes:
    """Validate face image file type and size"""
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid image type. Allowed: PNG, JPEG"
        )
    
    content = await file.read()
    
    if len(content) > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Image too large. Max size: 5MB"
        )
    
    return content
