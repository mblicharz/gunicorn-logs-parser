from datetime import datetime


class LogReader:
    def __init__(
            self,
            file_path: str,
            from_date: datetime,
            to_date: datetime
    ) -> None:
        self.file = file_path
        self.from_date = from_date
        self.to_date = to_date
        self._reader = self._read_file()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._reader)

    def _read_file(self):
        with open(self.file) as file_lines:
            next(file_lines)
            for file_line in file_lines:
                log_line = self._fetch_log_line(file_line)
                log_date_in_range = self._check_log_datetime(log_line)
                if log_date_in_range:
                    yield log_line

    def _fetch_log_line(self, file_line: str) -> str:
        return file_line.split(': ')[1]

    def _check_log_datetime(self, log: str) -> bool:
        log_date = self._get_datetime_from_log(log)

        date_in_range = False

        if self.from_date <= log_date <= self.to_date:
            date_in_range = True

        return date_in_range

    def _get_datetime_from_log(self, log: str) -> datetime:
        log_date = self._fetch_date_from_log(log)
        log_date = self._parse_to_datetime_without_timezone(log_date)
        return log_date

    def _fetch_date_from_log(self, log: str) -> str:
        return log[log.find('[') + 1: log.find(']')]

    def _parse_to_datetime_without_timezone(self, date: str) -> datetime:
        return datetime.strptime(date, '%d/%b/%Y:%H:%M:%S %z') \
            .replace(tzinfo=None)
