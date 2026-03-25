"""
Document Processing Routes
"""
from fastapi import APIRouter, Depends, UploadFile, File

from backend.app.core.dependencies import get_document_analysis_use_case
from backend.app.application.use_cases.document_analysis_use_case import DocumentAnalysisUseCase

router = APIRouter()


@router.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    use_case: DocumentAnalysisUseCase = Depends(get_document_analysis_use_case)
):
    """Analyze document using AWS Textract"""
    pass


@router.post("/extract-text")
async def extract_text(
    file: UploadFile = File(...),
    use_case: DocumentAnalysisUseCase = Depends(get_document_analysis_use_case)
):
    """Extract text from document"""
    pass
