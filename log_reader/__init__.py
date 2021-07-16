from datetime import datetime

from .log_reader import LogReader
from .statistic_collector import StatisticCollector
from .datetime_parser import parse_to_datetime


def read_log(
    file: str,
    from_date: datetime = None,
    to_date: datetime = None,
) -> None:
    reader = LogReader(file, from_date, to_date)
    sc = StatisticCollector()

    for line in reader:
        sc.add_line()

        if _is_status_code_2xx(int(line.status_code)):
            sc.add_response_len(int(line.response_len))

        sc.add_response(line.status_code)

        sc.add_request()

    _print_results(sc, reader)


def _is_status_code_2xx(status_code: int) -> bool:
    return 300 > status_code >= 200


def _print_results(sc: StatisticCollector, lr: LogReader) -> None:
    print(f"All lines: {sc.lines}")

    print(f"Requests: {sc.requests}")

    requests_per_sec = _count_requests_per_second(
        sc.requests, lr.first_date, lr.last_date
    )
    print(f"Requests per second: {requests_per_sec}")

    print(f"Responses: ({_format_responses_count(sc.get_responses())})")

    avg_size = _count_average_response_size(sc.average_response_len())
    print(f"avg size of 2xx responses: {avg_size} Mb")


def _count_requests_per_second(
    requests: int, from_date: datetime, to_date: datetime
) -> float:
    seconds = (to_date - from_date).total_seconds()
    return float("%.2f" % (requests / seconds))


def _format_responses_count(responses: dict) -> str:
    return ", ".join([f"{k}: {v}" for k, v in responses.items()])


def _count_average_response_size(avg_response_len: float) -> float:
    return float("%.2f" % (avg_response_len * 8 / 1024))


__all__ = ["parse_to_datetime", "read_log"]
