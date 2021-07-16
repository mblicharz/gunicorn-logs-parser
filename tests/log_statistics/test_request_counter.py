import pytest

from log_reader import RequestCounter, parse_to_datetime


@pytest.fixture()
def request_counter_obj() -> RequestCounter:
    return RequestCounter()


def test_RequestsCounter_for_proper_incrementation(request_counter_obj):
    request_counter_obj.update(1)
    assert request_counter_obj.count == 1
    request_counter_obj.update(5)
    assert request_counter_obj.count == 6


def test_RequestsCounter_for_requests_per_second_calculation(
        request_counter_obj):
    from_date = parse_to_datetime('20-11-2016_11-23-11')
    to_date = parse_to_datetime('20-11-2016_11-23-15')
    request_counter_obj.count = 40
    requests_per_sec = request_counter_obj.get_requests_per_second(from_date,
                                                                   to_date)
    assert requests_per_sec == 10
