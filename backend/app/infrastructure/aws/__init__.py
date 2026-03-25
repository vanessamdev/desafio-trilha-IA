"""
AWS Infrastructure Clients
"""
from backend.app.infrastructure.aws.textract_client import TextractClient
from backend.app.infrastructure.aws.rekognition_client import RekognitionClient
from backend.app.infrastructure.aws.bedrock_client import BedrockClient

__all__ = ["TextractClient", "RekognitionClient", "BedrockClient"]
