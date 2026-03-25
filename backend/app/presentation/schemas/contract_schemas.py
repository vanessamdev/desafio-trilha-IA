"""
Contract Analysis Schemas
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class DocumentDataResponse(BaseModel):
    raw_text: str
    fields: dict
    confidence: float
    pages_count: int


class FaceValidationResponse(BaseModel):
    is_valid: bool
    confidence: float
    faces_detected: int
    message: str


class AnalysisResponse(BaseModel):
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
    document_data: Optional[DocumentDataResponse] = None
    face_validation: Optional[FaceValidationResponse] = None
    analysis: Optional[AnalysisResponse] = None
    processed_at: datetime
    message: str
