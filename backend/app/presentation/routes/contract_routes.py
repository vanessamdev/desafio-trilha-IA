"""
Contract Analysis Routes
"""
from fastapi import APIRouter, Depends, UploadFile, File

from backend.app.presentation.schemas.contract_schemas import ContractAnalysisResponse
from backend.app.presentation.validators.file_validators import validate_document, validate_face_image
from backend.app.application.use_cases.contract_analysis_use_case import ContractAnalysisUseCase
from backend.app.core.dependencies import get_contract_analysis_use_case

router = APIRouter()


@router.post("/analyze-contract", response_model=ContractAnalysisResponse)
async def analyze_contract(
    document: UploadFile = File(..., description="Contract document (PDF or image)"),
    face_image: UploadFile = File(..., description="Face image for verification"),
    use_case: ContractAnalysisUseCase = Depends(get_contract_analysis_use_case)
) -> ContractAnalysisResponse:
    """
    Analyze contract document and verify face image.
    
    - Accepts PDF or image documents (max 10MB)
    - Accepts face image PNG/JPEG (max 5MB)
    """
    document_content = await validate_document(document)
    face_image_content = await validate_face_image(face_image)
    
    return await use_case.analyze(
        document_content=document_content,
        document_filename=document.filename,
        face_image_content=face_image_content,
        face_image_filename=face_image.filename
    )
