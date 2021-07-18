from datetime import datetime
from pathlib import Path
from typing import Iterator, Optional

from .log_line import LogLine
from .datetime_parser import parse_to_datetime_without_timezone


class LogReader:
    def __init__(
            self,
            file_path: str,
            from_date: Optional[datetime],
            to_date: Optional[datetime]
    ) -> None:
        self._validate_path(file_path)

        self.file = file_path
        self.from_date = from_date
        self.to_date = to_date

        self._reader = self._read_file()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._reader)

    @staticmethod
    def _validate_path(path: str) -> None:
        if not Path(path).is_file():
            raise FileNotFoundError

    def _read_file(self) -> Iterator:
        with open(self.file) as file_lines:
            next(file_lines)

            for file_line in file_lines:
                try:
                    yield self._get_log_line(file_line)
                except ValueError:
                    continue

    def _get_log_line(self, line: str) -> Optional[LogLine]:
        try:
            log_line = self._extract_log_line(line)
        except ValueError:
            return None

        edge_date_exists = self.from_date or self.to_date

        if not edge_date_exists or self._is_in_date_range(log_line):
            return log_line
        else:
            raise ValueError

    @staticmethod
    def _extract_log_line(file_line: str) -> LogLine:
        log_line = file_line.split(": ")[1]
        return LogLine(log_line)

    def _is_in_date_range(self, log_line: LogLine) -> bool:
        dt = parse_to_datetime_without_timezone(log_line.date)

        if not dt:
            return False

        dt_meets_from_date = not self.from_date or self.from_date <= dt
        dt_meets_to_date = not self.to_date or self.to_date >= dt

        return dt_meets_from_date and dt_meets_to_date
