"""
Contract Analysis Use Case
"""
import uuid
from typing import Optional
from datetime import datetime

from backend.app.domain.interfaces.document_extractor_interface import DocumentExtractorInterface
from backend.app.domain.interfaces.face_validator_interface import FaceValidatorInterface
from backend.app.domain.interfaces.ai_interpreter_interface import AIInterpreterInterface
from backend.app.presentation.schemas.contract_schemas import (
    ContractAnalysisResponse,
    DocumentDataResponse,
    FaceValidationResponse,
    AnalysisResponse
)


class ContractAnalysisUseCase:
    def __init__(
        self,
        document_extractor: DocumentExtractorInterface,
        face_validator: FaceValidatorInterface,
        ai_interpreter: AIInterpreterInterface
    ):
        self._document_extractor = document_extractor
        self._face_validator = face_validator
        self._ai_interpreter = ai_interpreter

    async def analyze(
        self,
        document_content: bytes,
        document_filename: str,
        face_image_content: Optional[bytes] = None,
        face_image_filename: Optional[str] = None
    ) -> ContractAnalysisResponse:
        """Orchestrate contract analysis workflow"""
        request_id = str(uuid.uuid4())
        
        document_data = await self._extract_document(document_content, document_filename)
        
        face_validation = None
        if face_image_content:
            face_validation = await self._validate_face(face_image_content)
        
        analysis = await self._interpret_contract(document_data.raw_text)
        
        return ContractAnalysisResponse(
            request_id=request_id,
            status="success",
            document_filename=document_filename,
            face_image_filename=face_image_filename,
            document_data=document_data,
            face_validation=face_validation,
            analysis=analysis,
            processed_at=datetime.utcnow(),
            message="Contract analysis completed successfully"
        )

    async def _extract_document(self, content: bytes, filename: str) -> DocumentDataResponse:
        """Extract data from document"""
        result = await self._document_extractor.extract(content, filename)
        return DocumentDataResponse(
            raw_text=result.raw_text,
            fields=result.fields,
            confidence=result.confidence,
            pages_count=result.pages_count
        )

    async def _validate_face(self, image_content: bytes) -> FaceValidationResponse:
        """Validate face in image"""
        result = await self._face_validator.validate(image_content)
        return FaceValidationResponse(
            is_valid=result.is_valid,
            confidence=result.confidence,
            faces_detected=result.faces_detected,
            message=result.message
        )

    async def _interpret_contract(self, extracted_text: str) -> AnalysisResponse:
        """Interpret contract using AI"""
        result = await self._ai_interpreter.interpret(extracted_text)
        return AnalysisResponse(
            summary=result.summary,
            risk_level=result.risk_level,
            recommendations=result.recommendations,
            is_valid_contract=result.is_valid_contract,
            confidence=result.confidence
        )
