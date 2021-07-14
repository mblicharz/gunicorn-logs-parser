import datetime


_date_format = '%d-%m-%Y'
_time_format = '%H-%M-%S'
_no_seconds_time_format = '%H-%M'


def datetime_T(datetime_str: str) -> str:
    date, time = datetime_str.split('_')
    _validate_date(date)
    _validate_time(time)

    return datetime_str


def _validate_date(date_str: str) -> None:
    try:
        datetime.datetime.strptime(date_str, _date_format)
    except ValueError:
        _print_error()


def _validate_time(time_str: str) -> None:
    try:
        datetime.datetime.strptime(time_str, _time_format)
    except ValueError:
        try:
            datetime.datetime.strptime(time_str, _no_seconds_time_format)
        except ValueError:
            _print_error()


def _print_error():
    print(f'Invalid date format. Valid formats:\n'
          f'DD-MM-YYYY_HH-MM-SS\nDD-MM-YYYY_HH-MM')
