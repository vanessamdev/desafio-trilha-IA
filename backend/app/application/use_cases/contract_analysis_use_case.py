"""
Contract Analysis Use Case
"""
import uuid
from datetime import datetime

from backend.app.domain.interfaces.document_extractor_interface import DocumentExtractorInterface
from backend.app.domain.interfaces.face_validator_interface import FaceValidatorInterface
from backend.app.domain.interfaces.ai_interpreter_interface import AIInterpreterInterface
from backend.app.presentation.schemas.contract_schemas import (
    ContractAnalysisResponse,
    ExtractedDataResponse,
    FaceValidationResponse,
    AIInterpretationResponse
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
        face_image_content: bytes,
        face_image_filename: str
    ) -> ContractAnalysisResponse:
        """Orchestrate contract analysis workflow"""
        request_id = str(uuid.uuid4())
        
        # Step 1: Extract document data
        extracted_data = await self._extract_document(document_content, document_filename)
        
        # Step 2: Validate face image
        face_validation = await self._validate_face(face_image_content)
        
        # Step 3: Interpret with AI
        ai_interpretation = await self._interpret_contract(extracted_data.raw_text)
        
        return self._build_response(
            request_id=request_id,
            document_filename=document_filename,
            face_image_filename=face_image_filename,
            extracted_data=extracted_data,
            face_validation=face_validation,
            ai_interpretation=ai_interpretation
        )

    async def _extract_document(self, content: bytes, filename: str) -> ExtractedDataResponse:
        """Extract data from document"""
        result = await self._document_extractor.extract(content, filename)
        return ExtractedDataResponse(
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

    async def _interpret_contract(self, extracted_text: str) -> AIInterpretationResponse:
        """Interpret contract using AI"""
        result = await self._ai_interpreter.interpret(extracted_text)
        return AIInterpretationResponse(
            summary=result.summary,
            risk_level=result.risk_level,
            recommendations=result.recommendations,
            is_valid_contract=result.is_valid_contract,
            confidence=result.confidence
        )

    def _build_response(
        self,
        request_id: str,
        document_filename: str,
        face_image_filename: str,
        extracted_data: ExtractedDataResponse,
        face_validation: FaceValidationResponse,
        ai_interpretation: AIInterpretationResponse
    ) -> ContractAnalysisResponse:
        """Build final response"""
        return ContractAnalysisResponse(
            request_id=request_id,
            status="completed",
            document_filename=document_filename,
            face_image_filename=face_image_filename,
            extracted_data=extracted_data,
            face_validation=face_validation,
            ai_interpretation=ai_interpretation,
            processed_at=datetime.utcnow(),
            message="Contract analysis completed successfully"
        )
