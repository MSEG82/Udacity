"""Base class with constructor and representation definition."""


class QuoteModel():
    """Class definition to get the message body and message author."""

    def __init__(self, body, author):
        """Instantiate the QuoteModel class."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of the class."""
        return f'<{self.body}, {self.author}>'
