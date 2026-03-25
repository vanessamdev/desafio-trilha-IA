"""
Text Generator Interface
"""
from abc import ABC, abstractmethod


class TextGeneratorInterface(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate text from prompt"""
        pass

    @abstractmethod
    async def summarize(self, text: str) -> str:
        """Summarize text"""
        pass
