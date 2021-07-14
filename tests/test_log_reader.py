from collections.abc import Iterable

import pytest

from datetime_type import datetime_T
from log_reader import LogReader
from tests import tools

logfile = tools.get_log_file()


def test_if_LogReader_object_is_iterable():
    log_reader = LogReader(logfile, None, None)
    assert isinstance(log_reader, Iterable)


def test_LogReader_FileNotFoundError_handled():
    try:
        log_reader = LogReader('file/that/not/exists', None, None)
        next(log_reader)
    except FileNotFoundError:
        pytest.fail("File not found not handled")


def test_LogReader_for_correct_number_of_records_with_defined_from_and_to_dates():
    from_date = datetime_T('30-11-2019_21-00-16')
    to_date = datetime_T('01-12-2019_11-06-07')
    log_reader = LogReader(logfile, from_date, to_date)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 10


def test_LogReader_for_correct_number_of_records_with_defined_from_date():
    from_date = datetime_T('30-11-2019_20-02-08')
    log_reader = LogReader(logfile, from_date, None)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 6


def test_LogReader_for_correct_number_of_records_with_defined_to_date():
    to_date = datetime_T('30-11-2019_20-02-08')
    log_reader = LogReader(logfile, None, to_date)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 8


def test_LogReader_for_correct_number_of_records_without_date_range():
    log_reader = LogReader('file/that/not/exists', None, None)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 13
