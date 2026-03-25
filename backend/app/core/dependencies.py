"""
Dependency Injection Container
"""
from functools import lru_cache

from backend.app.core.config import get_settings, Settings
from backend.app.infrastructure.aws.textract_client import TextractClient
from backend.app.infrastructure.aws.rekognition_client import RekognitionClient
from backend.app.infrastructure.aws.bedrock_client import BedrockClient
from backend.app.application.use_cases.document_analysis_use_case import DocumentAnalysisUseCase
from backend.app.application.use_cases.image_recognition_use_case import ImageRecognitionUseCase
from backend.app.application.use_cases.text_generation_use_case import TextGenerationUseCase


def get_config() -> Settings:
    """Provide settings dependency"""
    return get_settings()


@lru_cache()
def get_textract_client() -> TextractClient:
    """Provide Textract client dependency"""
    settings = get_settings()
    return TextractClient(region=settings.AWS_REGION)


@lru_cache()
def get_rekognition_client() -> RekognitionClient:
    """Provide Rekognition client dependency"""
    settings = get_settings()
    return RekognitionClient(region=settings.AWS_REGION)


@lru_cache()
def get_bedrock_client() -> BedrockClient:
    """Provide Bedrock client dependency"""
    settings = get_settings()
    return BedrockClient(region=settings.AWS_REGION)


def get_document_analysis_use_case() -> DocumentAnalysisUseCase:
    """Provide document analysis use case dependency"""
    return DocumentAnalysisUseCase(textract_client=get_textract_client())


def get_image_recognition_use_case() -> ImageRecognitionUseCase:
    """Provide image recognition use case dependency"""
    return ImageRecognitionUseCase(rekognition_client=get_rekognition_client())


def get_text_generation_use_case() -> TextGenerationUseCase:
    """Provide text generation use case dependency"""
    return TextGenerationUseCase(bedrock_client=get_bedrock_client())


def get_contract_analysis_use_case():
    """Provide contract analysis use case dependency"""
    from backend.app.application.use_cases.contract_analysis_use_case import ContractAnalysisUseCase
    return ContractAnalysisUseCase()
