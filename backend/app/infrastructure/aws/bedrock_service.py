"""
AWS Bedrock Service Implementation
"""
import json
import boto3
from botocore.exceptions import ClientError
from typing import Optional

from backend.app.domain.interfaces.ai_interpreter_interface import (
    AIInterpreterInterface,
    InterpretationResult
)
from backend.app.infrastructure.aws.exceptions import AWSServiceError


class BedrockService(AIInterpreterInterface):
    def __init__(self, region: str, model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0"):
        self._client = boto3.client("bedrock-runtime", region_name=region)
        self._model_id = model_id

    async def interpret(
        self, 
        extracted_text: str, 
        context: Optional[dict] = None
    ) -> InterpretationResult:
        """Analyze contract text using AWS Bedrock"""
        try:
            prompt = self._build_prompt(extracted_text, context)
            response = self._invoke_model(prompt)
            return self._parse_response(response)
        except ClientError as error:
            raise AWSServiceError(f"Bedrock error: {error.response['Error']['Message']}")

    def _build_prompt(self, text: str, context: Optional[dict]) -> str:
        """Build analysis prompt"""
        context_info = json.dumps(context) if context else "No additional context"
        
        return f"""Analyze the following contract document and provide a structured assessment.

Document text:
{text}

Additional context:
{context_info}

Provide your analysis in the following JSON format:
{{
    "summary": "Brief summary of the contract",
    "risk_level": "low|medium|high",
    "recommendations": ["recommendation 1", "recommendation 2"],
    "is_valid_contract": true|false,
    "confidence": 0.0-100.0
}}

Respond only with valid JSON."""

    def _invoke_model(self, prompt: str) -> dict:
        """Invoke Bedrock model"""
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        })
        
        response = self._client.invoke_model(
            modelId=self._model_id,
            body=body,
            contentType="application/json",
            accept="application/json"
        )
        
        response_body = json.loads(response["body"].read())
        return response_body

    def _parse_response(self, response: dict) -> InterpretationResult:
        """Parse Bedrock response into InterpretationResult"""
        try:
            content = response.get("content", [{}])[0].get("text", "{}")
            data = json.loads(content)
            
            return InterpretationResult(
                summary=data.get("summary", "Unable to generate summary"),
                risk_level=data.get("risk_level", "medium"),
                recommendations=data.get("recommendations", []),
                is_valid_contract=data.get("is_valid_contract", False),
                confidence=float(data.get("confidence", 0.0))
            )
        except (json.JSONDecodeError, KeyError, IndexError):
            return InterpretationResult(
                summary="Error parsing AI response",
                risk_level="high",
                recommendations=["Manual review required"],
                is_valid_contract=False,
                confidence=0.0
            )
