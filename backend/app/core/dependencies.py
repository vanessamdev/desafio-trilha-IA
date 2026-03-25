"""
Dependency Injection Container

Maps domain interfaces to concrete implementations.
Change USE_MOCK_SERVICES to switch between mock and AWS implementations.
"""
from functools import lru_cache

from backend.app.core.config import get_settings, Settings

# Domain Interfaces
from backend.app.domain.interfaces.document_extractor_interface import DocumentExtractorInterface
from backend.app.domain.interfaces.face_validator_interface import FaceValidatorInterface
from backend.app.domain.interfaces.ai_interpreter_interface import AIInterpreterInterface

# AWS Implementations
from backend.app.infrastructure.aws.textract_service import TextractService
from backend.app.infrastructure.aws.rekognition_service import RekognitionService
from backend.app.infrastructure.aws.bedrock_service import BedrockService

# Mock Implementations
from backend.app.infrastructure.services.mock_document_extractor import MockDocumentExtractor
from backend.app.infrastructure.services.mock_face_validator import MockFaceValidator
from backend.app.infrastructure.services.mock_ai_interpreter import MockAIInterpreter

# Use Cases
from backend.app.application.use_cases.contract_analysis_use_case import ContractAnalysisUseCase


def get_config() -> Settings:
    """Provide settings dependency"""
    return get_settings()


# =============================================================================
# Interface → Implementation Bindings
# =============================================================================

@lru_cache()
def get_document_extractor() -> DocumentExtractorInterface:
    """
    Bind: DocumentExtractorInterface → TextractService | MockDocumentExtractor
    """
    settings = get_settings()
    
    if settings.DEBUG:
        return MockDocumentExtractor()
    
    return TextractService(region=settings.AWS_REGION)


@lru_cache()
def get_face_validator() -> FaceValidatorInterface:
    """
    Bind: FaceValidatorInterface → RekognitionService | MockFaceValidator
    """
    settings = get_settings()
    
    if settings.DEBUG:
        return MockFaceValidator()
    
    return RekognitionService(region=settings.AWS_REGION)


@lru_cache()
def get_ai_interpreter() -> AIInterpreterInterface:
    """
    Bind: AIInterpreterInterface → BedrockService | MockAIInterpreter
    """
    settings = get_settings()
    
    if settings.DEBUG:
        return MockAIInterpreter()
    
    return BedrockService(region=settings.AWS_REGION)


# =============================================================================
# Use Case Providers
# =============================================================================

def get_contract_analysis_use_case() -> ContractAnalysisUseCase:
    """
    Provide ContractAnalysisUseCase with injected dependencies.
    
    Dependencies:
        - DocumentExtractorInterface → TextractService
        - FaceValidatorInterface → RekognitionService  
        - AIInterpreterInterface → BedrockService
    """
    return ContractAnalysisUseCase(
        document_extractor=get_document_extractor(),
        face_validator=get_face_validator(),
        ai_interpreter=get_ai_interpreter()
    )
