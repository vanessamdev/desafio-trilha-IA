"""
Dependency Injection Container
"""
from functools import lru_cache

from backend.app.core.config import settings
from backend.app.infrastructure.aws.textract_client import TextractClient
from backend.app.infrastructure.aws.rekognition_client import RekognitionClient
from backend.app.infrastructure.aws.bedrock_client import BedrockClient
from backend.app.application.use_cases.document_analysis_use_case import DocumentAnalysisUseCase
from backend.app.application.use_cases.image_recognition_use_case import ImageRecognitionUseCase
from backend.app.application.use_cases.text_generation_use_case import TextGenerationUseCase


@lru_cache()
def get_textract_client() -> TextractClient:
    return TextractClient(region=settings.AWS_REGION)


@lru_cache()
def get_rekognition_client() -> RekognitionClient:
    return RekognitionClient(region=settings.AWS_REGION)


@lru_cache()
def get_bedrock_client() -> BedrockClient:
    return BedrockClient(region=settings.AWS_REGION)


def get_document_analysis_use_case() -> DocumentAnalysisUseCase:
    return DocumentAnalysisUseCase(textract_client=get_textract_client())


def get_image_recognition_use_case() -> ImageRecognitionUseCase:
    return ImageRecognitionUseCase(rekognition_client=get_rekognition_client())


def get_text_generation_use_case() -> TextGenerationUseCase:
    return TextGenerationUseCase(bedrock_client=get_bedrock_client())
