import re
from typing import Sequence

VALID_LOG_FORMAT = r'([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (\d+)'


class LineReader:
    def __init__(self, line: str):
        self.line = line
        self.grouped_line = self._group_line(line)

    def _group_line(self, line: str) -> Sequence[str]:
        match = re.match(VALID_LOG_FORMAT, line)
        if not match:
            raise ValueError
        return match.groups()
