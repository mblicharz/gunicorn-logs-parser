from typing import Optional

from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics.abstract_statistic import AbstractStatistic


class AverageSizeSuccessfulResponses(AbstractStatistic):
    def __init__(self) -> None:
        self.responses = 0
        self.sum_size = 0

    def update(self, log_line: Optional[LogLine] = None) -> None:
        if 300 > int(log_line.status_code) >= 200:
            self.responses += 1
            self.sum_size += int(log_line.response_len)

    def get_result_repr(self) -> str:
        avg_size_as_bytes = self.sum_size / self.responses
        avg_size_as_megabits = avg_size_as_bytes * 8 / 1024 / 1024

        return f'{float("%.2f" % avg_size_as_megabits)} Mb'
