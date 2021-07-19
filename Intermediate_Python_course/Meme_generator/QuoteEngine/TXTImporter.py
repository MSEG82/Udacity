# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 07:45:36 2021

@author: U324451
"""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTImporter(IngestorInterface):
    importaciones = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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