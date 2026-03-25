"""
Mock AI Interpreter Implementation
"""
from backend.app.domain.interfaces.ai_interpreter_interface import (
    AIInterpreterInterface,
    InterpretationResult
)
from typing import Optional


class MockAIInterpreter(AIInterpreterInterface):
    async def interpret(
        self, 
        extracted_text: str, 
        context: Optional[dict] = None
    ) -> InterpretationResult:
        """Mock interpretation - returns simulated analysis"""
        return InterpretationResult(
            summary="Service agreement contract with standard terms. No unusual clauses detected.",
            risk_level="low",
            recommendations=[
                "Review payment terms before signing",
                "Verify party identification documents",
                "Confirm service delivery timeline"
            ],
            is_valid_contract=True,
            confidence=89.2
        )
