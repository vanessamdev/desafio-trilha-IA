"""
AWS Service Exceptions
"""


class AWSServiceError(Exception):
    """Base exception for AWS service errors"""
    
    def __init__(self, message: str, service: str = None, original_error: Exception = None):
        self.message = message
        self.service = service
        self.original_error = original_error
        super().__init__(self.message)


class TextractError(AWSServiceError):
    """Textract specific error"""
    
    def __init__(self, message: str, original_error: Exception = None):
        super().__init__(message, service="Textract", original_error=original_error)


class RekognitionError(AWSServiceError):
    """Rekognition specific error"""
    
    def __init__(self, message: str, original_error: Exception = None):
        super().__init__(message, service="Rekognition", original_error=original_error)


class BedrockError(AWSServiceError):
    """Bedrock specific error"""
    
    def __init__(self, message: str, original_error: Exception = None):
        super().__init__(message, service="Bedrock", original_error=original_error)
