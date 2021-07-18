from datetime import datetime
from config import statistics, output_template

from .log_reader import LogReader
from .statistic_collector import StatisticCollector
from .datetime_parser import parse_to_datetime


__all__ = ["parse_to_datetime", "read_log"]


def read_log(
    file: str,
    from_date: datetime = None,
    to_date: datetime = None,
) -> None:
    reader = LogReader(file, from_date, to_date)
    sc = StatisticCollector()

    for line in reader:
        try:
            sc.collect(line)
        except ValueError:
            continue

    _print_results(sc)


def _print_results(sc: StatisticCollector) -> None:
    placeholders = {}

    for statistic_name, statistic_cfg in statistics.items():
        placeholder = statistic_cfg.get('placeholder')

        if statistic_cfg.get('active'):
            result_repr = sc.statistics.get(statistic_name).get_result_repr()
        else:
            result_repr = 'inactive'

        placeholders.update({placeholder: result_repr})

    print(output_template.format(**placeholders))
