# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 07:59:45 2021

@author: U324451
"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TXTImporter import TXTImporter
from .CSVImporter import CSVImporter


class Ingestor(IngestorInterface):
    importers = [CSVImporter, TXTImporter]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)