import pytest

from datetime import datetime
from datetime_type import datetime_T

with_seconds_format = '%d-%m-%Y_%H-%M-%S'
no_seconds_format = '%d-%m-%Y_%H-%M'


def test_datetime_t_return_correct_type():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = datetime_T(datetime_str)
    assert isinstance(datetime_obj, datetime)


def test_datetime_T_return_valid_datetime():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = datetime.strptime(datetime_str, with_seconds_format)
    assert datetime_obj == datetime_T(datetime_str)


def test_datetime_T_return_invalid_datetime():
    datetime_str = '20-11-2016_11-23-11'
    datetime_obj = datetime.strptime(datetime_str, with_seconds_format)
    assert datetime_obj != datetime_T('20-11-2016_11-23-12')


def test_datetime_T_ValueError_handled_if_given_date_does_not_exists():
    datetime_str = '32-13-2016_11-23-11'
    try:
        datetime_obj = datetime_T(datetime_str)
    except ValueError:
        pytest.fail('Invalid datetime is not handled')


def test_datetime_T_ValueError_handled_if_invalid_date_format():
    datetime_str = '32/13/2016_11:23:11'
    try:
        datetime_obj = datetime_T(datetime_str)
    except ValueError:
        pytest.fail('Invalid datetime format is not handled')
