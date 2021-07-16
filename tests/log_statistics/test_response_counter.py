import pytest

from log_reader import ResponseCounter


@pytest.fixture()
def response_counter_obj():
    return ResponseCounter()


def test_ResponsesCounter_for_proper_output(response_counter_obj):
    response_counter_obj.update({200: 1, 201: 2, 404: 4})
    output = response_counter_obj.get_output()
    assert output == '(200: 1, 201: 2, 404: 4)'


def test_ResponsesCounter_for_proper_order_of_output(response_counter_obj):
    response_counter_obj.update({201: 2, 200: 1, 404: 4})
    output = response_counter_obj.get_output()
    assert output == '(200: 1, 201: 2, 404: 4)'
