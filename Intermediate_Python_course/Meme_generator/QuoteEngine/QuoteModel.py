# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:49:59 2021

@author: U324451
"""

"""Base class with constructor and representation definition."""


class QuoteModel():
    """Class definition to get the message body and message auther."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of the class."""
        return f'<{self.body}, {self.author}>'