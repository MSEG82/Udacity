"""This code serves for ingestion of info in CSV format."""


from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """Class CSVImporter.

    This class works with csv type files, parses the quote and author
    and returns the QuoteModel object.
    """

    importaciones = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV type file.

        The classmethod 'parse()' extract the 'quote' and 'author'
        return the list of QuoteModel.
        Parameters:
            path (str) : path of the csv file.
        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
