"""
Contract Analysis Schemas
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ExtractedDataResponse(BaseModel):
    raw_text: str
    fields: dict
    confidence: float
    pages_count: int


class FaceValidationResponse(BaseModel):
    is_valid: bool
    confidence: float
    faces_detected: int
    message: str


class AIInterpretationResponse(BaseModel):
    summary: str
    risk_level: str
    recommendations: List[str]
    is_valid_contract: bool
    confidence: float


class ContractAnalysisResponse(BaseModel):
    request_id: str
    status: str
    document_filename: str
    face_image_filename: str
    extracted_data: Optional[ExtractedDataResponse] = None
    face_validation: Optional[FaceValidationResponse] = None
    ai_interpretation: Optional[AIInterpretationResponse] = None
    processed_at: datetime
    message: str
