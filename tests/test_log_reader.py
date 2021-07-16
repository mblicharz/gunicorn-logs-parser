import pytest

from collections.abc import Iterable
from log_reader.datetime_parser import parse_to_datetime
from log_reader import LogReader
from tests.common import log_file_path


def test_if_LogReader_object_is_iterable():
    log_reader = LogReader(log_file_path, None, None)
    assert isinstance(log_reader, Iterable)


def test_LogReader_FileNotFoundError_handled():
    with pytest.raises(FileNotFoundError):
        log_reader = LogReader('file/that/not/exists', None, None)


def test_LogReader_for_correct_number_of_records_with_defined_from_and_to_dates():
    from_date = parse_to_datetime('30-11-2019_21-00-16')
    to_date = parse_to_datetime('01-12-2019_11-06-07')
    log_reader = LogReader(log_file_path, from_date, to_date)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 6


def test_LogReader_for_correct_number_of_records_with_defined_from_date():
    from_date = parse_to_datetime('30-11-2019_20-02-08')
    log_reader = LogReader(log_file_path, from_date, None)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 7


def test_LogReader_for_correct_number_of_records_with_defined_to_date():
    to_date = parse_to_datetime('30-11-2019_20-02-08')
    log_reader = LogReader(log_file_path, None, to_date)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 7


def test_LogReader_for_correct_number_of_records_without_date_range():
    log_reader = LogReader(log_file_path, None, None)
    counter = 0
    for _ in log_reader:
        counter += 1
    assert counter == 13
