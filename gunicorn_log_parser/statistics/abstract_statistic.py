from abc import ABC, abstractmethod
from typing import Optional

from gunicorn_log_parser.log_line import LogLine


class AbstractStatistic(ABC):
    @abstractmethod
    def update(self, log_line: Optional[LogLine] = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_result_repr(self) -> str:
        raise NotImplementedError
