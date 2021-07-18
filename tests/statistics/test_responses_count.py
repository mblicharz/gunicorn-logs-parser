import pytest

from gunicorn_log_parser.log_line import LogLine
from gunicorn_log_parser.statistics import ResponsesCodesCount
from tests.common import single_200_log_line, single_404_log_line


@pytest.fixture()
def responses_count_obj() -> ResponsesCodesCount:
    return ResponsesCodesCount()


@pytest.fixture()
def log_line_200_obj() -> LogLine:
    return LogLine(
        raw_log_line=single_200_log_line.get('line'),
        log_format=single_200_log_line.get('format')
    )


@pytest.fixture()
def log_line_404_obj() -> LogLine:
    return LogLine(
        raw_log_line=single_404_log_line.get('line'),
        log_format=single_404_log_line.get('format')
    )


def test_ResponsesCount_update(
        responses_count_obj,
        log_line_200_obj,
        log_line_404_obj
):
    responses_count_obj.update(log_line_200_obj)
    responses_count_obj.update(log_line_404_obj)

    assert responses_count_obj.responses_codes == {200: 1, 404: 1}


def test_ResponsesCount_result_repr(
        responses_count_obj,
        log_line_200_obj,
        log_line_404_obj
):
    responses_count_obj.update(log_line_200_obj)
    responses_count_obj.update(log_line_404_obj)

    assert responses_count_obj.get_result_repr() == '(200: 1, 404: 1)'
