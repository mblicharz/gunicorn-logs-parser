import pytest

from gunicorn_log_parser.log_reader import LogLine
from tests import common


def test_LineReader_raising_ValueError_if_bad_line_format():
    with pytest.raises(ValueError):
        line_reader = LogLine('some bad line')


@pytest.fixture()
def line_with_output() -> dict:
    return common.log_line_with_splitted_output


@pytest.fixture()
def line_reader_obj(line_with_output) -> LogLine:
    return LogLine(line_with_output['line'])


@pytest.fixture()
def grouped_output(line_with_output) -> tuple:
    return line_with_output['output']


def test_LineReader_correct_fetching_data_from_log_line(line_reader_obj,
                                                        grouped_output):
    assert line_reader_obj.line == grouped_output


def test_LineReader_for_proper_fields_assignation(line_reader_obj,
                                                  grouped_output):
    assert line_reader_obj.remote_address == grouped_output[0]
    assert line_reader_obj.user_name == grouped_output[1]
    assert line_reader_obj.date == grouped_output[2]
    assert line_reader_obj.status_line == grouped_output[3]
    assert line_reader_obj.status_code == grouped_output[4]
    assert line_reader_obj.response_len == grouped_output[5]
    assert line_reader_obj.referer == grouped_output[6]
    assert line_reader_obj.user_agent == grouped_output[7]
    assert line_reader_obj.time == grouped_output[8]
