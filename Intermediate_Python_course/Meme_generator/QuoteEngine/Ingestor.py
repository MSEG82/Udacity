"""This code serves for parsing all the different
types of documents included in 'importers':
pdf, docs, txt and csv.
""""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter
from .CSVImporter import CSVImporter


class Ingestor(IngestorInterface):
    importers = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse files of any of the defined types.

        The classmethod 'parse()' extract the 'quote' and 'author'
        return the list of QuoteModel.
        Parameters:
            cls : IngestorInterface class
            path (str) : path of the TXT file.
        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
