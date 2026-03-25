"""
Document Extractor Interface
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ExtractedData:
    raw_text: str
    fields: dict
    confidence: float
    pages_count: int


class DocumentExtractorInterface(ABC):
    @abstractmethod
    async def extract(self, content: bytes, filename: str) -> ExtractedData:
        """Extract text and structured data from document"""
        pass
