"""This module defines the interface for quote file ingestors."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for all ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return True if the file has a supported extension."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse a file and return QuoteModel instances."""
        pass
