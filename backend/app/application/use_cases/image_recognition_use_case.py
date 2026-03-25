"""
Image Recognition Use Case
"""
from backend.app.domain.interfaces.image_recognizer_interface import ImageRecognizerInterface
from backend.app.domain.entities.image import Image


class ImageRecognitionUseCase:
    def __init__(self, rekognition_client: ImageRecognizerInterface):
        self._rekognition_client = rekognition_client

    async def detect_labels(self, image: Image) -> list:
        """Detect labels in image"""
        pass

    async def detect_faces(self, image: Image) -> list:
        """Detect faces in image"""
        pass
