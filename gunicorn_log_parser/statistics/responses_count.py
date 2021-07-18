from collections import Counter
from typing import Optional

from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics.abstract_statistic import AbstractStatistic


class ResponsesCount(AbstractStatistic):
    def __init__(self) -> None:
        self.responses = Counter()

    def update(self, log_line: Optional[LogLine] = None) -> None:
        self.responses.update({int(log_line.status_code): 1})

    def get_result_repr(self) -> str:
        responses_repr = ', '.join([f'{k}: {v}' for k, v in self.responses.items()])
        return f'({responses_repr})'
