# languages/base_parser.py
class BaseParser:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def parse_comments(self):
        """Diese Methode sollte in den abgeleiteten Klassen überschrieben werden."""
        raise NotImplementedError("Diese Methode muss in einem Subparser implementiert werden.")

