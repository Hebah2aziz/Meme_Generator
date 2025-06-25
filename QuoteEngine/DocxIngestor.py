"""
docx_ingestor module.

This module provides functionality to parse DOCX files and extract
quotes into QuoteModel instances using the python-docx library.
"""

import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """A concrete ingestor class to parse DOCX files containing quotes."""

    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is '.docx'.

        Args:
            path (str): The file path.

        Returns:
            bool: True if the file is a DOCX, False otherwise.
        """
        return path.lower().endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a DOCX file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the DOCX file.

        Returns:
            List[QuoteModel]: List of QuoteModel objects parsed from the file.
        """
        doc = docx.Document(path)
        quotes = []
        for para in doc.paragraphs:
            if para.text and '-' in para.text:
                body, author = para.text.strip().split(' - ')
                quotes.append(QuoteModel(body.strip('" '), author.strip()))
        return quotes
