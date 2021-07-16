from datetime import datetime

import pytest

from log_reader import StatisticCollector


@pytest.fixture()
def sc_obj() -> StatisticCollector:
    return StatisticCollector()


def test_counting_all_lines(sc_obj):
    assert sc_obj.lines == 0

    sc_obj.add_line()
    assert sc_obj.lines == 1

    for _ in range(0, 3):
        sc_obj.add_line()

    assert sc_obj.lines == 4


def test_counting_failures(sc_obj):
    assert sc_obj.failures == 0

    sc_obj.add_failure()
    assert sc_obj.failures == 1

    for _ in range(0, 3):
        sc_obj.add_failure()

    assert sc_obj.failures == 4


def test_collecting_requests(sc_obj):
    assert sc_obj.requests == 0

    sc_obj.add_request()
    assert sc_obj.requests == 1

    for _ in range(0, 3):
        sc_obj.add_request()

    assert sc_obj.requests == 4


def test_collecting_responses(sc_obj):
    assert sc_obj.get_responses() == {}

    sc_obj.add_response(200)
    assert sc_obj.get_responses() == {200: 1}

    sc_obj.add_response(200)
    sc_obj.add_response(404)
    sc_obj.add_response(500)
    assert sc_obj.get_responses() == {
        200: 2,
        404: 1,
        500: 1
    }

    sc_obj.add_response(101)
    assert sc_obj.get_responses() == {
        101: 1,
        200: 2,
        404: 1,
        500: 1
    }


def test_calculating_average_len_of_response(sc_obj):
    assert sc_obj.average_response_len() == 0

    sc_obj.add_request()
    sc_obj.add_response_len(720)
    assert sc_obj.average_response_len() == 720

    sc_obj.add_request()
    sc_obj.add_response_len(720)
    sc_obj.add_request()
    sc_obj.add_response_len(1280)
    assert sc_obj.average_response_len() == 906.67
