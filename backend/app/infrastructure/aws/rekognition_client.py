"""
AWS Rekognition Client
"""
from typing import List
from backend.app.domain.interfaces.image_recognizer_interface import ImageRecognizerInterface
from backend.app.domain.entities.image import Image


class RekognitionClient(ImageRecognizerInterface):
    def __init__(self, region: str):
        self._region = region
        self._client = None  # boto3 client will be initialized here

    async def detect_labels(self, image: Image) -> List[dict]:
        """Detect labels in image using AWS Rekognition"""
        pass

    async def detect_faces(self, image: Image) -> List[dict]:
        """Detect faces in image using AWS Rekognition"""
        pass
