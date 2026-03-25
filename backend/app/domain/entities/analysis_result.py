"""
Analysis Result Entity
"""
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import Enum

from backend.app.domain.entities.document_data import DocumentData
from backend.app.domain.entities.face_match_result import FaceMatchResult


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AnalysisStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AIInterpretation:
    summary: str
    risk_level: RiskLevel
    recommendations: list[str] = field(default_factory=list)
    is_valid_contract: bool = False
    confidence: float = 0.0


@dataclass
class AnalysisResult:
    id: str
    status: AnalysisStatus
    document_data: Optional[DocumentData] = None
    face_match: Optional[FaceMatchResult] = None
    ai_interpretation: Optional[AIInterpretation] = None
    error_message: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    
    def is_approved(self) -> bool:
        """Check if analysis result meets approval criteria"""
        if not self._has_all_components():
            return False
        
        return (
            self.document_data.is_high_confidence() and
            self.face_match.is_valid and
            self.ai_interpretation.is_valid_contract and
            self.ai_interpretation.risk_level != RiskLevel.HIGH
        )
    
    def _has_all_components(self) -> bool:
        """Check if all analysis components are present"""
        return all([
            self.document_data,
            self.face_match,
            self.ai_interpretation
        ])
    
    def get_risk_level(self) -> RiskLevel:
        """Get overall risk level"""
        if not self.ai_interpretation:
            return RiskLevel.HIGH
        return self.ai_interpretation.risk_level
    
    def mark_completed(self) -> None:
        """Mark analysis as completed"""
        self.status = AnalysisStatus.COMPLETED
        self.completed_at = datetime.utcnow()
    
    def mark_failed(self, error: str) -> None:
        """Mark analysis as failed"""
        self.status = AnalysisStatus.FAILED
        self.error_message = error
        self.completed_at = datetime.utcnow()
