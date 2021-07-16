import pytest

from collections.abc import Iterable
from log_reader.datetime_parser import parse_to_datetime
from log_reader.datetime_parser import parse_to_datetime_without_timezone
from log_reader.log_reader import LogReader
from tests import common
from tests.common import log_file_path


def test_if_LogReader_object_is_iterable():
    log_reader = LogReader(log_file_path, None, None)
    assert isinstance(log_reader, Iterable)


def test_LogReader_FileNotFoundError_handled():
    with pytest.raises(FileNotFoundError):
        LogReader('file/that/not/exists', None, None)


def test_LogReader_for_correct_number_of_records_with_defined_from_and_to_dates():
    from_date = parse_to_datetime('30-11-2019_21-00-16')
    to_date = parse_to_datetime('01-12-2019_11-06-07')
    log_reader = LogReader(log_file_path, from_date, to_date)
    for line in log_reader:
        dt = parse_to_datetime_without_timezone(line.date)
        assert from_date <= dt <= to_date


def test_LogReader_for_correct_number_of_records_with_defined_from_date():
    from_date = parse_to_datetime('30-11-2019_20-02-08')
    log_reader = LogReader(log_file_path, from_date, None)
    for line in log_reader:
        dt = parse_to_datetime_without_timezone(line.date)
        assert from_date <= dt


def test_LogReader_for_correct_number_of_records_with_defined_to_date():
    to_date = parse_to_datetime('30-11-2019_20-02-08')
    log_reader = LogReader(log_file_path, None, to_date)
    for line in log_reader:
        dt = parse_to_datetime_without_timezone(line.date)
        assert dt <= to_date


def test_LogReader_for_correct_number_of_records_without_date_range():
    log_reader = LogReader(log_file_path, None, None)

    read_lines = 0
    for _ in log_reader:
        read_lines += 1

    assert common.log_file_lines_count == read_lines
