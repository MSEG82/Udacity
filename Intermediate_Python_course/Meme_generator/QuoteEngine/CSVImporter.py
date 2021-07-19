# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 07:36:28 2021

@author: U324451
"""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    importaciones = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():             
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes