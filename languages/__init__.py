# languages/__init__.py

from .c_cpp_parser import CCppParser
from .javascript_parser import JavaScriptParser
from .go_parser import GoParser
from .rust_parser import RustParser
from .python_parser import PythonParser  # Falls du einen Python-Parser hast
from .swift_parser import SwiftParser  # Falls du einen Swift-Parser hinzugefügt hast

# Exportiere alle Parser für einfacheren Zugriff
__all__ = [
    'CCppParser',
    'JavaScriptParser',
    'GoParser',
    'RustParser',
    'PythonParser',
    'SwiftParser'
]
