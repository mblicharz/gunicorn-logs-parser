from datetime import datetime
from pathlib import Path

from .datetime_parser import parse_to_datetime_without_timezone


class LogReader:
    def __init__(
            self,
            file_path: str,
            from_date: datetime,
            to_date: datetime
    ) -> None:
        self._validate_path(file_path)

        self.file = file_path
        self.from_date = from_date
        self.to_date = to_date
        self.first_date = None
        self.last_date = None

        self._reader = self._read_file()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._reader)

    @staticmethod
    def _validate_path(path: str) -> None:
        if not Path(path).is_file():
            raise FileNotFoundError

    def _read_file(self):
        with open(self.file) as file_lines:
            next(file_lines)

            for file_line in file_lines:
                log_line = self._extract_log_line(file_line)

                self._set_first_and_last_date(log_line)

                edge_date_exists = self.from_date or self.to_date

                if not edge_date_exists or self._is_in_date_range(log_line):
                    yield log_line

    def _set_first_and_last_date(self, log_line: str) -> None:
        if not self.last_date:
            self.last_date = self._get_datetime(log_line)
        self.first_date = self._get_datetime(log_line)

    @staticmethod
    def _extract_log_line(file_line: str) -> str:
        return file_line.split(': ')[1]

    def _is_in_date_range(self, log_line: str) -> bool:
        log_date = self._get_datetime(log_line)

        if not log_date:
            return False

        in_range = not self.from_date or self.from_date <= log_date \
            and not self.to_date or self.to_date >= log_date

        return in_range

    def _get_datetime(self, log: str) -> datetime:
        log_date = self._extract_date(log)
        log_date = parse_to_datetime_without_timezone(log_date)
        return log_date

    @staticmethod
    def _extract_date(log: str) -> str:
        return log[log.find('[') + 1: log.find(']')]
