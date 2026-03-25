"""
Document Data Entity
"""
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import Enum


class DocumentType(Enum):
    CONTRACT = "contract"
    INVOICE = "invoice"
    IDENTITY = "identity"
    OTHER = "other"


@dataclass
class DocumentData:
    id: str
    filename: str
    content_type: str
    raw_text: str
    extracted_fields: dict = field(default_factory=dict)
    confidence: float = 0.0
    pages_count: int = 1
    document_type: DocumentType = DocumentType.OTHER
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    def is_high_confidence(self, threshold: float = 80.0) -> bool:
        """Check if extraction confidence meets threshold"""
        return self.confidence >= threshold
    
    def has_required_fields(self, required: list[str]) -> bool:
        """Check if document contains all required fields"""
        return all(field in self.extracted_fields for field in required)
    
    def get_field(self, field_name: str, default: str = "") -> str:
        """Get extracted field value"""
        return self.extracted_fields.get(field_name, default)
