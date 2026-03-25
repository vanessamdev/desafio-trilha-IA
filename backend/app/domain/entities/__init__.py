"""
Domain Entities
"""
from backend.app.domain.entities.document import Document
from backend.app.domain.entities.image import Image
from backend.app.domain.entities.document_data import DocumentData, DocumentType
from backend.app.domain.entities.face_match_result import FaceMatchResult, FaceMatchStatus
from backend.app.domain.entities.analysis_result import AnalysisResult, AnalysisStatus, RiskLevel, AIInterpretation

__all__ = [
    "Document",
    "Image",
    "DocumentData",
    "DocumentType",
    "FaceMatchResult",
    "FaceMatchStatus",
    "AnalysisResult",
    "AnalysisStatus",
    "RiskLevel",
    "AIInterpretation"
]
