import pytest

from gunicorn_log_parser.log_reader import LogReader
from gunicorn_log_parser.statistics import RequestsPerSecond
from gunicorn_log_parser.datetime_parser import \
    parse_to_datetime_without_timezone
from tests.common import log_file_path


@pytest.fixture()
def log_format() -> str:
    return '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'


@pytest.fixture()
def requests_per_second_obj(log_format) -> RequestsPerSecond:
    rps = RequestsPerSecond()
    log_reader = LogReader(
        log_file_path,
        parse_to_datetime_without_timezone('01/Dec/2019:11:05:29 +0100'),
        None
    )
    for log_line in log_reader:
        rps.update(log_line)

    return rps


def test_RequestsPerSecond_update(requests_per_second_obj):
    assert requests_per_second_obj.requests == 5

    first_date = parse_to_datetime_without_timezone(
        '01/Dec/2019:11:05:29 +0100'
    )
    assert requests_per_second_obj.first_date == first_date

    last_date = parse_to_datetime_without_timezone(
        '01/Dec/2019:11:06:07 +0100'
    )
    assert requests_per_second_obj.last_date == last_date


def test_RequestsPerSecond_result_repr(requests_per_second_obj):
    assert requests_per_second_obj.get_result_repr() == '0.13/sec'
