"""
Document Entity
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Document:
    id: str
    filename: str
    content_type: str
    content: bytes
    created_at: datetime
    extracted_text: Optional[str] = None
    metadata: Optional[dict] = None
