import sys

from config import statistics

from gunicorn_log_parser.log_line import LogLine


class StatisticCollector:
    def __init__(self):
        self.statistics = {}

        self._prepare()

    def _prepare(self) -> None:
        for statistic_name, statistic_cfg in statistics.items():
            if not statistic_cfg.get('active'):
                continue

            statistic = statistics.get(statistic_name).get('class')

            try:
                self.statistics.update({statistic_name: statistic()})
            except TypeError:
                sys.exit(f'Error in config: {statistic_name}[class].'
                         f' Class not found.')

    def collect(self, log_line: LogLine) -> None:
        if not log_line:
            raise ValueError

        for obj in self.statistics.values():
            obj.update(log_line)

