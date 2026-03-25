"""
Mock Document Extractor Implementation
"""
from backend.app.domain.interfaces.document_extractor_interface import (
    DocumentExtractorInterface,
    ExtractedData
)


class MockDocumentExtractor(DocumentExtractorInterface):
    async def extract(self, content: bytes, filename: str) -> ExtractedData:
        """Mock extraction - returns simulated data"""
        return ExtractedData(
            raw_text="[Mock] Contract between Party A and Party B. Terms and conditions apply.",
            fields={
                "contract_type": "Service Agreement",
                "parties": ["Party A", "Party B"],
                "date": "2024-01-15",
                "value": "R$ 10.000,00"
            },
            confidence=92.5,
            pages_count=3
        )
