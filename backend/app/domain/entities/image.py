"""
Image Entity
"""
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Image:
    id: str
    filename: str
    content_type: str
    content: bytes
    created_at: datetime
    labels: Optional[List[str]] = None
    metadata: Optional[dict] = None
