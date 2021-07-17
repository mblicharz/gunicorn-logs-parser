import re
from typing import Sequence, Optional

DEFAULT_LOG_FORMAT = r'%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

DEFAULT_LOG_FORMAT_REGEX = (
    r'([(\d\.)]+) - (.*?) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (\d+)'
)

FORMAT_IDENTIFIERS_REGEX = {
    "%(h)s": r'"?([(\d\.)]+)"?',
    "%(l)s": r'"?-"?',
    "%(u)s": r'"?(.*?)"?',
    "%(t)s": r'"?\[(.*?)\]"?',
    "%(r)s": r'"?(.*?)"?',
    "%(s)s": r'"?(\d+)"?',
    "%(b)s": r'"?(\d+)"?',
    "%(f)s": r'"?(.*?)"?',
    "%(a)s": r'"?(.*?)"?',
    "%(D)s": r'"?(\d+)"?',
}

FORMAT_IDENTIFIERS_ATTRIBUTES = {
    "%(h)s": "remote_address",
    "%(u)s": "user_name",
    "%(t)s": "date",
    "%(r)s": "status_line",
    "%(s)s": "status_code",
    "%(b)s": "response_len",
    "%(f)s": "referer",
    "%(a)s": "user_agent",
    "%(D)s": "time",
}


class LogLine:
    def __init__(
            self,
            raw_log_line: str,
            log_format: Optional[str] = DEFAULT_LOG_FORMAT
    ) -> None:
        self.format = log_format
        self.line = self._split_line(raw_log_line, log_format)

        self._fetch_data()

    def _split_line(self, line: str, log_format: str) -> Sequence[str]:
        regex = self._parse_log_format_to_regex(log_format)
        match = re.match(regex, line)
        if not match:
            raise ValueError
        return match.groups()

    def _parse_log_format_to_regex(self, log_format: str) -> str:
        log_format = self._remove_double_quotations(log_format)

        identifiers_regex = []

        for identifier in log_format.split(" "):
            identifiers_regex.append(FORMAT_IDENTIFIERS_REGEX.get(identifier))

        regex = " ".join(identifiers_regex)
        regex += '$'

        return regex

    def _fetch_data(self):
        data = list(self.line)
        log_format = self._remove_double_quotations(self.format)

        for identifier in log_format.split(" "):
            if identifier == '%(l)s':
                continue

            setattr(
                self,
                FORMAT_IDENTIFIERS_ATTRIBUTES.get(identifier),
                data.pop(0)
            )

    @staticmethod
    def _remove_double_quotations(string: str) -> str:
        return string.translate(str.maketrans("", "", '"'))
