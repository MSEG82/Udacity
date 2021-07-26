"""This code serves for ingestion of info in TXT format."""


from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTImporter(IngestorInterface):
    """Class TXTImporter.

    This class works with txt type files, parses the quote and author
    and returns the QuoteModel object.
    """

    importaciones = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT type file.

        The classmethod 'parse()' extract the 'quote' and 'author'
        return the list of QuoteModel.
        Parameters:
            path (str) : path of the TXT file.
        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        file_ref = open(path, "r")

        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        return quotes
