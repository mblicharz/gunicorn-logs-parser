import pytest

from log_reader import ResponsesCounter


@pytest.fixture()
def responses_counter_obj():
    return ResponsesCounter()


def test_ResponsesCounter_for_proper_output(responses_counter_obj):
    responses_counter_obj.update({200: 1, 201: 2, 404: 4})
    output = responses_counter_obj.get_output()
    assert output == '(200: 1, 201: 2, 404: 4)'


def test_ResponsesCounter_for_proper_order_of_output(responses_counter_obj):
    responses_counter_obj.update({201: 2, 200: 1, 404: 4})
    output = responses_counter_obj.get_output()
    assert output == '(200: 1, 201: 2, 404: 4)'
