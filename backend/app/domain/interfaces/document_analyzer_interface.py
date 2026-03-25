"""
Document Analyzer Interface
"""
from abc import ABC, abstractmethod
from backend.app.domain.entities.document import Document


class DocumentAnalyzerInterface(ABC):
    @abstractmethod
    async def analyze(self, document: Document) -> dict:
        """Analyze document and return structured data"""
        pass

    @abstractmethod
    async def extract_text(self, document: Document) -> str:
        """Extract text from document"""
        pass
