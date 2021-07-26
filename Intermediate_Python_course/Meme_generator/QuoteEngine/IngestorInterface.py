"""IngestorInterface class.

Defines the abstract class IngestorInterface that
makes it possible to use methods 'can_ingest' and 'parse'.
"""


from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class IngestorInterface."""

    importaciones = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Cheks the possibility to ingest files files of a given type.

        The classmethod 'can_ingest()' .
        Parameters:
            cls : IngestorInterface class
            path (str) : path of the TXT file.
        Return:
            Boolean wether it can be ingested or not
        """
        ext = path.split('.')[-1]
        return ext in cls.importaciones

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse files of any of the defined types.

        The classmethod 'parse()' extract the 'quote' and 'author'
        return the list of QuoteModel.
        Parameters:
            cls : IngestorInterface class
            path (str) : path of the given file.
        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        pass
