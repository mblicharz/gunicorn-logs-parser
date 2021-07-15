import pytest

from log_reader import AverageCounter


@pytest.fixture()
def average_counter_obj() -> AverageCounter:
    return AverageCounter()


def test_AverageCounter_for_counting_items(average_counter_obj):
    assert average_counter_obj.items_count == 0
    average_counter_obj.add(1000)
    average_counter_obj.add(1500)
    average_counter_obj.add(2000)
    assert average_counter_obj.items_count == 3


def test_AverageCounter_for_counting_average(average_counter_obj):
    average_counter_obj.add(1000)
    average_counter_obj.add(1500)
    average_counter_obj.add(2000)
    assert average_counter_obj.average() == 1500
