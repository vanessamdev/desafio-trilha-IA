"""
Contract Analyzer Interface
"""
from abc import ABC, abstractmethod
from backend.app.presentation.schemas.contract_schemas import ContractAnalysisResponse


class ContractAnalyzerInterface(ABC):
    @abstractmethod
    async def analyze(
        self,
        document_content: bytes,
        document_filename: str,
        face_image_content: bytes,
        face_image_filename: str
    ) -> ContractAnalysisResponse:
        """Analyze contract document and face image"""
        pass
