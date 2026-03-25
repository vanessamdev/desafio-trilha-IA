"""
Application Exceptions
"""
from typing import Optional


class AppException(Exception):
    """Base application exception"""
    
    def __init__(
        self, 
        message: str, 
        status_code: int = 500,
        error_code: Optional[str] = None
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code or "INTERNAL_ERROR"
        super().__init__(self.message)


class ValidationError(AppException):
    """Validation error"""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=400, error_code="VALIDATION_ERROR")


class FileUploadError(AppException):
    """File upload error"""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=400, error_code="FILE_UPLOAD_ERROR")


class AWSServiceError(AppException):
    """AWS service error"""
    
    def __init__(self, message: str, service: str):
        super().__init__(
            message=f"{service}: {message}",
            status_code=502,
            error_code=f"AWS_{service.upper()}_ERROR"
        )


class DocumentExtractionError(AWSServiceError):
    """Document extraction error"""
    
    def __init__(self, message: str):
        super().__init__(message, service="Textract")


class FaceValidationError(AWSServiceError):
    """Face validation error"""
    
    def __init__(self, message: str):
        super().__init__(message, service="Rekognition")


class AIInterpretationError(AWSServiceError):
    """AI interpretation error"""
    
    def __init__(self, message: str):
        super().__init__(message, service="Bedrock")
