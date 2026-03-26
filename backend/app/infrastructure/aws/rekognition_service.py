"""
AWS Rekognition Service Implementation
"""
import boto3
from botocore.exceptions import ClientError

from backend.app.domain.interfaces.face_validator_interface import (
    FaceValidatorInterface,
    FaceValidationResult
)
from backend.app.infrastructure.aws.exceptions import AWSServiceError


class RekognitionService(FaceValidatorInterface):
    def __init__(self, region: str, access_key: str = None, secret_key: str = None, similarity_threshold: float = 80.0):
        self._client = boto3.client(
            "rekognition",
            region_name=region,
            aws_access_key_id=access_key if access_key else None,
            aws_secret_access_key=secret_key if secret_key else None
        )
        self._similarity_threshold = similarity_threshold

    async def validate(self, image_content: bytes) -> FaceValidationResult:
        """Detect and validate faces in image"""
        try:
            response = self._client.detect_faces(
                Image={"Bytes": image_content},
                Attributes=["ALL"]
            )
            
            faces = response.get("FaceDetails", [])
            faces_count = len(faces)
            
            if faces_count == 0:
                return FaceValidationResult(
                    is_valid=False,
                    confidence=0.0,
                    faces_detected=0,
                    message="No face detected in image"
                )
            
            if faces_count > 1:
                return FaceValidationResult(
                    is_valid=False,
                    confidence=faces[0].get("Confidence", 0.0),
                    faces_detected=faces_count,
                    message="Multiple faces detected. Please provide image with single face"
                )
            
            confidence = faces[0].get("Confidence", 0.0)
            return FaceValidationResult(
                is_valid=True,
                confidence=confidence,
                faces_detected=1,
                message="Face detected and validated successfully"
            )
        except ClientError as error:
            raise AWSServiceError(f"Rekognition error: {error.response['Error']['Message']}")

    async def compare_faces(
        self, 
        source_image: bytes, 
        target_image: bytes
    ) -> FaceValidationResult:
        """Compare faces between source and target images"""
        try:
            response = self._client.compare_faces(
                SourceImage={"Bytes": source_image},
                TargetImage={"Bytes": target_image},
                SimilarityThreshold=self._similarity_threshold
            )
            
            matches = response.get("FaceMatches", [])
            
            if not matches:
                return FaceValidationResult(
                    is_valid=False,
                    confidence=0.0,
                    faces_detected=len(response.get("UnmatchedFaces", [])),
                    message="Faces do not match"
                )
            
            best_match = max(matches, key=lambda x: x.get("Similarity", 0))
            similarity = best_match.get("Similarity", 0.0)
            
            return FaceValidationResult(
                is_valid=similarity >= self._similarity_threshold,
                confidence=similarity,
                faces_detected=len(matches),
                message=f"Face match found with {similarity:.1f}% similarity"
            )
        except ClientError as error:
            raise AWSServiceError(f"Rekognition error: {error.response['Error']['Message']}")
