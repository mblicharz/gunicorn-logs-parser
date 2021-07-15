import pytest

from log_reader import RequestsCounter, parse_to_datetime


@pytest.fixture()
def requests_counter_obj() -> RequestsCounter:
    return RequestsCounter()


def test_RequestsCounter_for_proper_incrementation(requests_counter_obj):
    requests_counter_obj.update(1)
    assert requests_counter_obj.count == 1
    requests_counter_obj.update(5)
    assert requests_counter_obj.count == 6


def test_RequestsCounter_for_requests_per_second_calculation(
        requests_counter_obj):
    from_date = parse_to_datetime('20-11-2016_11-23-11')
    to_date = parse_to_datetime('20-11-2016_11-23-15')
    requests_counter_obj.count = 40
    requests_per_sec = requests_counter_obj.get_requests_per_second(from_date,
                                                                    to_date)
    assert requests_per_sec == 10
