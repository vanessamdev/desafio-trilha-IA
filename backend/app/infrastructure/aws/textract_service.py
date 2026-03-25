"""
AWS Textract Service Implementation
"""
import boto3
from botocore.exceptions import ClientError

from backend.app.domain.interfaces.document_extractor_interface import (
    DocumentExtractorInterface,
    ExtractedData
)
from backend.app.infrastructure.aws.exceptions import AWSServiceError


class TextractService(DocumentExtractorInterface):
    def __init__(self, region: str):
        self._client = boto3.client("textract", region_name=region)

    async def extract(self, content: bytes, filename: str) -> ExtractedData:
        """Extract text and data from document using AWS Textract"""
        try:
            response = self._client.analyze_document(
                Document={"Bytes": content},
                FeatureTypes=["FORMS", "TABLES"]
            )
            
            raw_text = self._extract_raw_text(response)
            fields = self._extract_fields(response)
            confidence = self._calculate_confidence(response)
            pages_count = response.get("DocumentMetadata", {}).get("Pages", 1)
            
            return ExtractedData(
                raw_text=raw_text,
                fields=fields,
                confidence=confidence,
                pages_count=pages_count
            )
        except ClientError as error:
            raise AWSServiceError(f"Textract error: {error.response['Error']['Message']}")

    def _extract_raw_text(self, response: dict) -> str:
        """Extract raw text from Textract response"""
        lines = []
        for block in response.get("Blocks", []):
            if block.get("BlockType") == "LINE":
                lines.append(block.get("Text", ""))
        return "\n".join(lines)

    def _extract_fields(self, response: dict) -> dict:
        """Extract key-value pairs from Textract response"""
        fields = {}
        key_map, value_map, block_map = self._build_block_maps(response)
        
        for block_id, key_block in key_map.items():
            value_block = self._find_value_block(key_block, value_map, block_map)
            key_text = self._get_text(key_block, block_map)
            value_text = self._get_text(value_block, block_map) if value_block else ""
            if key_text:
                fields[key_text] = value_text
        
        return fields

    def _build_block_maps(self, response: dict) -> tuple:
        """Build maps for efficient block lookup"""
        key_map = {}
        value_map = {}
        block_map = {}
        
        for block in response.get("Blocks", []):
            block_id = block.get("Id")
            block_map[block_id] = block
            
            if block.get("BlockType") == "KEY_VALUE_SET":
                if "KEY" in block.get("EntityTypes", []):
                    key_map[block_id] = block
                else:
                    value_map[block_id] = block
        
        return key_map, value_map, block_map

    def _find_value_block(self, key_block: dict, value_map: dict, block_map: dict) -> dict:
        """Find value block associated with key block"""
        for relationship in key_block.get("Relationships", []):
            if relationship.get("Type") == "VALUE":
                for value_id in relationship.get("Ids", []):
                    if value_id in value_map:
                        return value_map[value_id]
        return None

    def _get_text(self, block: dict, block_map: dict) -> str:
        """Get text from block"""
        if not block:
            return ""
        
        text_parts = []
        for relationship in block.get("Relationships", []):
            if relationship.get("Type") == "CHILD":
                for child_id in relationship.get("Ids", []):
                    child_block = block_map.get(child_id, {})
                    if child_block.get("BlockType") == "WORD":
                        text_parts.append(child_block.get("Text", ""))
        
        return " ".join(text_parts)

    def _calculate_confidence(self, response: dict) -> float:
        """Calculate average confidence from response"""
        confidences = []
        for block in response.get("Blocks", []):
            if "Confidence" in block:
                confidences.append(block["Confidence"])
        
        return sum(confidences) / len(confidences) if confidences else 0.0
