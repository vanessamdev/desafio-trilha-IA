"""
AWS Textract Client
"""
from backend.app.domain.interfaces.document_analyzer_interface import DocumentAnalyzerInterface
from backend.app.domain.entities.document import Document


class TextractClient(DocumentAnalyzerInterface):
    def __init__(self, region: str):
        self._region = region
        self._client = None  # boto3 client will be initialized here

    async def analyze(self, document: Document) -> dict:
        """Analyze document using AWS Textract"""
        pass

    async def extract_text(self, document: Document) -> str:
        """Extract text from document using AWS Textract"""
        pass
