"""
ingestor module.

Provides the Ingestor class that delegates file parsing to specific ingestor
classes based on file type (e.g., TXT, CSV, DOCX, PDF).
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """
    A concrete ingestor that uses appropriate sub-ingestors to parse files.

    Delegates parsing responsibility to specialized ingestors for supported
    formats: TXT, CSV, DOCX, and PDF.
    """

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if any sub-ingestor can handle the given file path.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if an ingestor can handle the file, False otherwise.
        """
        return any(ing.can_ingest(path) for ing in cls.ingestors)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file using the first matching sub-ingestor.

        Args:
            path (str): The path to the file to parse.

        Returns:
            List[QuoteModel]: A list of parsed QuoteModel instances.

        Raises:
            ValueError: If no ingestor can handle the file type.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"File format not supported: {path}")
