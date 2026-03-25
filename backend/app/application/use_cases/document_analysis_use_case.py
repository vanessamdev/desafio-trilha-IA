"""
Document Analysis Use Case
"""
from backend.app.domain.interfaces.document_analyzer_interface import DocumentAnalyzerInterface
from backend.app.domain.entities.document import Document


class DocumentAnalysisUseCase:
    def __init__(self, textract_client: DocumentAnalyzerInterface):
        self._textract_client = textract_client

    async def analyze(self, document: Document) -> dict:
        """Analyze document and extract information"""
        pass

    async def extract_text(self, document: Document) -> str:
        """Extract text from document"""
        pass
