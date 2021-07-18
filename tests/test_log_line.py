import pytest

from gunicorn_log_parser.log_line import LogLine
from tests import common


def test_LogLine_different_formats():
    examples = common.get_examples_log_formats_with_lines()
    correct_results = common.correct_results_examples

    for log_format, line in examples.items():
        try:
            log_line = LogLine(line, log_format)
        except ValueError:
            pytest.fail('Unexpected ValueError')

        assert log_line.line in correct_results
