from datetime import datetime
from pathlib import Path


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

            # TODO: Move to external function and spread on smaller functions
            # TODO: Check time execution
            # TODO: Change log_line to raw_log_line
            for file_line in file_lines:
                log_line = self._fetch_log_line(file_line)

                self._set_first_and_last_date(log_line)

                edge_date_exists = self.from_date or self.to_date

                if not edge_date_exists or self._is_log_in_date_range(log_line):
                    yield log_line

    def _set_first_and_last_date(self, log_line: str) -> None:
        if not self.last_date:
            self.last_date = self._get_datetime_from_log(log_line)
        self.first_date = self._get_datetime_from_log(log_line)

    def _fetch_log_line(self, file_line: str) -> str:
        return file_line.split(': ')[1]

    # TODO: Change for shorter name
    def _is_log_in_date_range(self, log_line: str) -> bool:
        log_date = self._get_datetime_from_log(log_line)

        # TODO: PLEASE, change this horrible names
        from_meet = False
        to_meet = False

        if not self.from_date or self.from_date <= log_date:
            from_meet = True

        if not self.to_date or self.to_date >= log_date:
            to_meet = True

        return from_meet and to_meet

    def _get_datetime_from_log(self, log: str) -> datetime:
        log_date = self._fetch_date_from_log(log)
        log_date = self._parse_to_datetime_without_timezone(log_date)
        return log_date

    def _fetch_date_from_log(self, log: str) -> str:
        return log[log.find('[') + 1: log.find(']')]

    def _parse_to_datetime_without_timezone(self, date: str) -> datetime:
        date_format = '%d/%b/%Y:%H:%M:%S %z'
        return datetime.strptime(date, date_format).replace(tzinfo=None)
