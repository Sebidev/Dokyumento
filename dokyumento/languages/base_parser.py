# languages/base_parser.py
class BaseParser:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def parse_comments(self):
        """This method should be overridden in the derived classes."""
        raise NotImplementedError("This method must be implemented in a subparser.")

