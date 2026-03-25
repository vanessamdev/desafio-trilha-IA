"""
Domain Interfaces
"""
from backend.app.domain.interfaces.document_analyzer_interface import DocumentAnalyzerInterface
from backend.app.domain.interfaces.image_recognizer_interface import ImageRecognizerInterface
from backend.app.domain.interfaces.text_generator_interface import TextGeneratorInterface
from backend.app.domain.interfaces.repository_interface import RepositoryInterface

__all__ = [
    "DocumentAnalyzerInterface",
    "ImageRecognizerInterface",
    "TextGeneratorInterface",
    "RepositoryInterface"
]
