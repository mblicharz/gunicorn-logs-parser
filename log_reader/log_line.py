import re
from typing import Sequence

VALID_LOG_FORMAT = r'([(\d\.)]+) - (.*?) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (\d+)'


class LogLine:
    def __init__(self, raw_log_line: str):
        self.line = self._split_line(raw_log_line)

        self.remote_address = self.line[0]
        self.user_name = self.line[1]
        self.date = self.line[2]
        self.status_line = self.line[3]
        self.status_code = self.line[4]
        self.response_len = self.line[5]
        self.referer = self.line[6]
        self.user_agent = self.line[7]
        self.time = self.line[8]

    @staticmethod
    def _split_line(line: str) -> Sequence[str]:
        match = re.match(VALID_LOG_FORMAT, line)
        if not match:
            raise ValueError
        return match.groups()
