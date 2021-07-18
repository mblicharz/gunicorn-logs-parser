import pytest

from gunicorn_log_parser.log_reader import LogReader
from gunicorn_log_parser.datetime_parser import \
    parse_to_datetime_without_timezone
from gunicorn_log_parser.statistics import AverageSizeSuccessfulResponses
from tests.common import log_file_path


@pytest.fixture()
def log_format() -> str:
    return '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'


@pytest.fixture()
def average_size_obj(log_format) -> AverageSizeSuccessfulResponses:
    average_size = AverageSizeSuccessfulResponses()
    log_reader = LogReader(
        log_file_path,
        parse_to_datetime_without_timezone('01/Dec/2019:11:05:29 +0100'),
        None
    )
    for log_line in log_reader:
        average_size.update(log_line)

    return average_size


def test_AverageSizeSuccessfulResponses_update(average_size_obj):
    assert average_size_obj.responses == 2
    assert average_size_obj.sum_size == 1440


def test_AverageSizeSuccessfulResponses_result_repr(average_size_obj):
    try:
        assert average_size_obj.get_result_repr() == '0.01 Mb'
    except ZeroDivisionError:
        pytest.fail()
