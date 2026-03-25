"""
Face Match Result Entity
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class FaceMatchStatus(Enum):
    MATCHED = "matched"
    NOT_MATCHED = "not_matched"
    NO_FACE_DETECTED = "no_face_detected"
    MULTIPLE_FACES = "multiple_faces"
    ERROR = "error"


@dataclass
class FaceMatchResult:
    is_valid: bool
    confidence: float
    faces_detected: int
    status: FaceMatchStatus
    message: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    def is_high_confidence_match(self, threshold: float = 90.0) -> bool:
        """Check if face match confidence meets threshold"""
        return self.is_valid and self.confidence >= threshold
    
    def is_single_face(self) -> bool:
        """Check if exactly one face was detected"""
        return self.faces_detected == 1
    
    @classmethod
    def no_face(cls) -> "FaceMatchResult":
        """Factory for no face detected result"""
        return cls(
            is_valid=False,
            confidence=0.0,
            faces_detected=0,
            status=FaceMatchStatus.NO_FACE_DETECTED,
            message="No face detected in image"
        )
    
    @classmethod
    def multiple_faces(cls, count: int) -> "FaceMatchResult":
        """Factory for multiple faces detected result"""
        return cls(
            is_valid=False,
            confidence=0.0,
            faces_detected=count,
            status=FaceMatchStatus.MULTIPLE_FACES,
            message=f"Multiple faces detected: {count}"
        )
