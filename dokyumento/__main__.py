import os
import sys
from dokyumento.languages.c_cpp_parser import CCppParser
from dokyumento.languages.javascript_parser import JavaScriptParser
from dokyumento.languages.typescript_parser import TypeScriptParser
from dokyumento.languages.go_parser import GoParser
from dokyumento.languages.rust_parser import RustParser
from dokyumento.languages.python_parser import PythonParser
from dokyumento.languages.swift_parser import SwiftParser

PARSERS = {
    '.c': CCppParser,
    '.cpp': CCppParser,
    '.js': JavaScriptParser,
    '.ts': TypeScriptParser,
    '.go': GoParser,
    '.rs': RustParser,
    '.swift': SwiftParser,
    # Additional assignments can be added here
}

def scan_directory(directory):
    """Scans the directory for files and processes them with the appropriate parser."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1]
            parser_class = PARSERS.get(ext)
            if parser_class:
                filepath = os.path.join(root, file)
                print(f"Scanning file: {filepath}")  # Debugging
                parser = parser_class(filepath)
                comments = parser.parse_comments()
                print(f"Comments found: {comments}")  # Debugging
                if comments:
                    output_to_markdown(filepath, comments)


def output_to_markdown(filepath, comments):
    """Writes the extracted comments to a Markdown file."""
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    markdown_filename = os.path.join(directory, f"{filename}.md")
    print(f"Creating markdown file: {markdown_filename}")  # Debugging
    try:
        with open(markdown_filename, 'w') as md_file:
            md_file.write(f"# {filename}\n\n")
            for comment in comments:
                md_file.write(f"{comment}\n\n")
        print(f"Markdown file created: {markdown_filename}")  # Debugging
    except Exception as e:
        print(f"Error writing markdown file: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m dokyumento <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        sys.exit(1)

    scan_directory(directory)

if __name__ == "__main__":
    main()
