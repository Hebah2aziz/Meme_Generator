"""This module defines the abstract base class for quote ingestors."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for all quote ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the file extension is supported.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if extension is in allowed_extensions.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file and return a list of QuoteModel instances.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: Parsed quotes.
        """
        pass
