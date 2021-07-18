from typing import Optional

from gunicorn_log_parser.datetime_parser import \
    parse_to_datetime_without_timezone
from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics.abstract_statistic import AbstractStatistic


class RequestsPerSecond(AbstractStatistic):
    def __init__(self) -> None:
        self.requests = 0
        self.first_date = None
        self.last_date = None

    def update(self, log_line: Optional[LogLine] = None) -> None:
        self.first_date = parse_to_datetime_without_timezone(log_line.date)

        if not self.last_date:
            self.last_date = parse_to_datetime_without_timezone(log_line.date)

        self.requests += 1

    def get_result_repr(self) -> str:
        diff_secs = (self.last_date - self.first_date).total_seconds()

        try:
            avg = self.requests / diff_secs
        except ZeroDivisionError:
            # returns the number of requests because no seconds have elapsed
            avg = self.requests

        return f'{float("%.2f" % avg)}/sec'
