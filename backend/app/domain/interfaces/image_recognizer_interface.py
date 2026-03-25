"""
Image Recognizer Interface
"""
from abc import ABC, abstractmethod
from typing import List
from backend.app.domain.entities.image import Image


class ImageRecognizerInterface(ABC):
    @abstractmethod
    async def detect_labels(self, image: Image) -> List[dict]:
        """Detect labels in image"""
        pass

    @abstractmethod
    async def detect_faces(self, image: Image) -> List[dict]:
        """Detect faces in image"""
        pass
