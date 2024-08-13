# languages/python_parser.py
import re
from .base_parser import BaseParser

class PythonParser(BaseParser):
    def parse_comments(self):
        comments = []
        in_multiline_comment = False
        multiline_comment_buffer = []

        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()

                if in_multiline_comment:
                    end_multiline_comment = re.search(r'"""', line)
                    if end_multiline_comment:
                        in_multiline_comment = False
                        multiline_comment_buffer.append(line[:end_multiline_comment.start()].strip())
                        comments.append(' '.join(multiline_comment_buffer).strip())
                        multiline_comment_buffer = []
                    else:
                        multiline_comment_buffer.append(line)
                else:
                    start_multiline_comment = re.search(r'"""', line)
                    if start_multiline_comment:
                        in_multiline_comment = True
                        multiline_comment_buffer.append(line[start_multiline_comment.end():].strip())
                        continue
                    start_multiline_comment = re.search(r"'''", line)
                    if start_multiline_comment:
                        in_multiline_comment = True
                        multiline_comment_buffer.append(line[start_multiline_comment.end():].strip())
                        continue

                    single_line_comment = re.match(r'^\s*#\s*(.*)', line)
                    if single_line_comment:
                        comments.append(single_line_comment.group(1).strip())

        return comments
