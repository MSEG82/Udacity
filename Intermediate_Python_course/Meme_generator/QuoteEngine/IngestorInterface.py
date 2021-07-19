# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:52:58 2021

@author: U324451
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    
    importaciones = []
    
    @classmethod    
    def can_ingest(cls, path: str) -> bool:       
        ext =  path.split('.')[-1]
        return ext in cls.importaciones      
    
    @classmethod        
    @abstractmethod        
    def parse(cls, path:str) -> List[QuoteModel]:
        pass
    
    