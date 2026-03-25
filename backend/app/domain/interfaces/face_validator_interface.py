"""
Face Validator Interface
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class FaceValidationResult:
    is_valid: bool
    confidence: float
    faces_detected: int
    message: str


class FaceValidatorInterface(ABC):
    @abstractmethod
    async def validate(self, image_content: bytes) -> FaceValidationResult:
        """Validate face in image"""
        pass

    @abstractmethod
    async def compare_faces(
        self, 
        source_image: bytes, 
        target_image: bytes
    ) -> FaceValidationResult:
        """Compare faces between two images"""
        pass
