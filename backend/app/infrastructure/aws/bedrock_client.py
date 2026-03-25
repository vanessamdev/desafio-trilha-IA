"""
AWS Bedrock Client
"""
from backend.app.domain.interfaces.text_generator_interface import TextGeneratorInterface


class BedrockClient(TextGeneratorInterface):
    def __init__(self, region: str):
        self._region = region
        self._client = None  # boto3 client will be initialized here

    async def generate(self, prompt: str) -> str:
        """Generate text using AWS Bedrock"""
        pass

    async def summarize(self, text: str) -> str:
        """Summarize text using AWS Bedrock"""
        pass
