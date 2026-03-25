"""
Text Generation Use Case
"""
from backend.app.domain.interfaces.text_generator_interface import TextGeneratorInterface


class TextGenerationUseCase:
    def __init__(self, bedrock_client: TextGeneratorInterface):
        self._bedrock_client = bedrock_client

    async def generate(self, prompt: str) -> str:
        """Generate text using AI model"""
        pass

    async def summarize(self, text: str) -> str:
        """Summarize text using AI model"""
        pass
