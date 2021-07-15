import re
from typing import Sequence

VALID_LOG_FORMAT = r'([(\d\.)]+) - (.*?) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (\d+)'


class LineReader:
    def __init__(self, line: str):
        self.line = line
        self.grouped_line = self._group_line(line)

        self.remote_address = self.grouped_line[0]
        self.user_name = self.grouped_line[1]
        self.date = self.grouped_line[2]
        self.status_line = self.grouped_line[3]
        self.status_code = self.grouped_line[4]
        self.response_len = self.grouped_line[5]
        self.referer = self.grouped_line[6]
        self.user_agent = self.grouped_line[7]
        self.time = self.grouped_line[8]

    def _group_line(self, line: str) -> Sequence[str]:
        match = re.match(VALID_LOG_FORMAT, line)
        if not match:
            raise ValueError
        return match.groups()
