"""
AI Interpreter Interface
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class InterpretationResult:
    summary: str
    risk_level: str  # low, medium, high
    recommendations: list[str]
    is_valid_contract: bool
    confidence: float


class AIInterpreterInterface(ABC):
    @abstractmethod
    async def interpret(
        self, 
        extracted_text: str, 
        context: Optional[dict] = None
    ) -> InterpretationResult:
        """Interpret extracted document data using AI"""
        pass
