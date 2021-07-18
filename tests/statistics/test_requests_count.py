from gunicorn_log_parser.statistics import RequestsCount


def test_RequestsCount_counting():
    rc = RequestsCount()

    assert rc.requests == 0

    rc.update()

    assert rc.requests == 1

    rc.update()
    rc.update()
    rc.update()

    assert rc.requests == 4


def test_RequestsCount_result_repr():
    rc = RequestsCount()

    assert rc.get_result_repr() == '0'
