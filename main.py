"""
main.py.

This module handles data ingestion logic for various file types and demonstrates
the use of the Ingestor and MemeEngine classes.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from MemeEngine.MemeEngine import MemeEngine


class Ingestor(IngestorInterface):
    """
    Ingestor is a base class that provides methods to determine whether a file.
    
    can be ingested and to parse its contents.
    """

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the given file can be ingested based on its file extension.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        return any(ing.can_ingest(path) for ing in cls.ingestors)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and extract its contents.

        Args:
            path (str): The path to the file to be parsed.

        Returns:
            List[QuoteModel]: A list of extracted QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"File format not supported: {path}")


# Test Ingestor
if __name__ == "__main__":
    quotes = Ingestor.parse("_data/SimpleLines/SimpleLines.txt")
    for quote in quotes:
        print(quote)

    # Test MemeEngine
    meme = MemeEngine('./output')
    path = meme.make_meme(
        './_data/photos/dog/dog1.jpg',
        "Life is what happens",
        "John Lennon"
    )
    print(f"Meme saved at: {path}")
