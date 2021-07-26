"""This code serves for ingestion of info in DOCX format."""


from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    """Class DocxImporter.

    This class works with docx type files, parses the quote and author
    and returns the QuoteModel object.
    """

    importaciones = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX type file.

        The classmethod 'parse()' extract the 'quote' and 'author'
        return the list of QuoteModel.
        Parameters:
            path (str) : path of the docx file.
        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
