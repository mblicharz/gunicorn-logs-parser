from typing import Optional

from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics.abstract_statistic import AbstractStatistic


class RequestsCount(AbstractStatistic):
    def __init__(self):
        super().__init__()

        self.requests = 0

    def update(self, log_line: Optional[LogLine] = None) -> None:
        self.requests += 1

    def get_result_repr(self) -> str:
        return str(self.requests)
