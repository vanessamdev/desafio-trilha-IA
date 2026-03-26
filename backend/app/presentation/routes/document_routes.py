"""
Document Processing Routes
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/analyze")
async def analyze_document():
    """Analyze document using AWS Textract"""
    return {"message": "Use /analyze-contract endpoint"}


@router.post("/extract-text")
async def extract_text():
    """Extract text from document"""
    return {"message": "Use /analyze-contract endpoint"}
