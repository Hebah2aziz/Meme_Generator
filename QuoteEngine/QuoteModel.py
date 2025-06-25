"""This module defines the QuoteModel class for representing quotes."""


class QuoteModel:
    """A simple class to encapsulate a quote with its body and author."""

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel instance.

        Args:
            body (str): The text of the quote.
            author (str): The person who said or wrote the quote.
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """
        Return a string representation of the quote.

        Returns:
            str: A formatted string like '"Quote text" - Author'.
        """
        return f'"{self.body}" - {self.author}'
