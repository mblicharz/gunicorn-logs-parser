from collections import Counter
from typing import Optional

from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics.abstract_statistic import AbstractStatistic


class ResponsesCodesCount(AbstractStatistic):
    def __init__(self) -> None:
        self.responses_codes = Counter()

    def update(self, log_line: Optional[LogLine] = None) -> None:
        self.responses_codes.update({int(log_line.status_code): 1})

    def get_result_repr(self) -> str:
        responses_codes_repr = ', '.join(
            [f'{k}: {v}' for k, v in self.responses_codes.items()]
        )
        return f'({responses_codes_repr})'
