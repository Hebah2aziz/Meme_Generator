"""
pdf_ingestor module.

This module provides functionality to parse PDF files and extract quotes
into QuoteModel instances using the pdftotext utility.
"""

import subprocess
import os
from typing import List
from tempfile import TemporaryDirectory
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """A concrete ingestor to parse PDF files and extract quotes."""

    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is '.pdf'.

        Args:
            path (str): The file path.

        Returns:
            bool: True if the file is a PDF, False otherwise.
        """
        return path.lower().endswith('.pdf')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a PDF file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the PDF file.

        Returns:
            List[QuoteModel]: A list of quotes extracted from the PDF.
        """
        quotes = []
        with TemporaryDirectory() as tmpdir:
            temp_txt = os.path.join(tmpdir, "output.txt")
            subprocess.run(['pdftotext', path, temp_txt], check=True)

            with open(temp_txt, 'r') as file:
                for line in file:
                    if '-' in line:
                        body, author = line.strip().split(' - ')
                        quotes.append(QuoteModel(body.strip('" '), author.strip()))
        return quotes
