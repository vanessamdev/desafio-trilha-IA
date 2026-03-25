"""
Contract Analysis Schemas
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ContractAnalysisResponse(BaseModel):
    request_id: str
    status: str
    document_filename: str
    face_image_filename: str
    extracted_text: Optional[str] = None
    face_match_confidence: Optional[float] = None
    processed_at: datetime
    message: str
