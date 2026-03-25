"""
Image Repository Implementation
"""
from typing import Optional, List
from backend.app.domain.interfaces.repository_interface import RepositoryInterface
from backend.app.domain.entities.image import Image


class ImageRepository(RepositoryInterface[Image]):
    def __init__(self):
        self._storage = {}  # In-memory storage placeholder

    async def save(self, entity: Image) -> Image:
        """Save image"""
        pass

    async def find_by_id(self, entity_id: str) -> Optional[Image]:
        """Find image by ID"""
        pass

    async def find_all(self) -> List[Image]:
        """Find all images"""
        pass

    async def delete(self, entity_id: str) -> bool:
        """Delete image by ID"""
        pass
