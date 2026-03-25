"""
Generic Repository Interface
"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class RepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    async def save(self, entity: T) -> T:
        """Save entity"""
        pass

    @abstractmethod
    async def find_by_id(self, entity_id: str) -> Optional[T]:
        """Find entity by ID"""
        pass

    @abstractmethod
    async def find_all(self) -> List[T]:
        """Find all entities"""
        pass

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        """Delete entity by ID"""
        pass
