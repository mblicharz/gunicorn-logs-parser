import pytest

from datetime import datetime
from log_reader.datetime_parser import parse_to_datetime

with_seconds_format = '%d-%m-%Y_%H-%M-%S'
no_seconds_format = '%d-%m-%Y_%H-%M'


def test_parse_to_datetime_return_correct_type():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = parse_to_datetime(datetime_str)
    assert isinstance(datetime_obj, datetime)


def test_parse_to_datetime_return_valid_datetime():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = datetime.strptime(datetime_str, with_seconds_format)
    assert datetime_obj == parse_to_datetime(datetime_str)


def test_parse_to_datetime_return_invalid_datetime():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = datetime.strptime(datetime_str, with_seconds_format)
    assert datetime_obj != parse_to_datetime('20-11-2016_11-23-12')


def test_parse_to_datetime_ValueError_handled_if_given_date_does_not_exists():
    datetime_str = '32-13-2016_11-23-11'
    try:
        datetime_obj = parse_to_datetime(datetime_str)
    except ValueError:
        pytest.fail('Invalid datetime is not handled')


def test_parse_to_datetime_ValueError_handled_if_invalid_date_format():
    datetime_str = '32/13/2016_11:23:11'
    try:
        datetime_obj = parse_to_datetime(datetime_str)
    except ValueError:
        pytest.fail('Invalid datetime format is not handled')
