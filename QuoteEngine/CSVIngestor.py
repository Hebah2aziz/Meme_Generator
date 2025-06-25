"""
csv_ingestor module.

This module ingests quotes from CSV files by implementing the CSVIngestor class,
which parses the file and returns QuoteModel instances.
"""

import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """A concrete ingestor class to parse CSV files containing quotes."""

    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is '.csv'.

        Args:
            path (str): The file path.

        Returns:
            bool: True if the file is a CSV, False otherwise.
        """
        return path.lower().endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a CSV file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: List of QuoteModel objects parsed from the file.
        """
        df = pd.read_csv(path)
        return [QuoteModel(row['body'], row['author']) for _, row in df.iterrows()]