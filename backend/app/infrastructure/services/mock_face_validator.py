"""
Mock Face Validator Implementation
"""
from backend.app.domain.interfaces.face_validator_interface import (
    FaceValidatorInterface,
    FaceValidationResult
)


class MockFaceValidator(FaceValidatorInterface):
    async def validate(self, image_content: bytes) -> FaceValidationResult:
        """Mock validation - returns simulated result"""
        return FaceValidationResult(
            is_valid=True,
            confidence=97.3,
            faces_detected=1,
            message="Face detected and validated successfully"
        )

    async def compare_faces(
        self, 
        source_image: bytes, 
        target_image: bytes
    ) -> FaceValidationResult:
        """Mock comparison - returns simulated result"""
        return FaceValidationResult(
            is_valid=True,
            confidence=95.8,
            faces_detected=2,
            message="Faces match with high confidence"
        )
