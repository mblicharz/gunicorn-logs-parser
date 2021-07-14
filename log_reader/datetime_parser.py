from datetime import datetime

_format = '%d-%m-%Y_%H-%M-%S'
_no_seconds_format = '%d-%m-%Y_%H-%M'


def parse_to_datetime(datetime_str: str) -> datetime:
    dt = None

    try:
        dt = datetime.strptime(datetime_str, _format)
    except ValueError:
        try:
            dt = datetime.strptime(datetime_str, _no_seconds_format)
        except ValueError:
            _print_error()

    return dt


def _print_error():
    print(f'Invalid date format. Valid formats:\n'
          f'DD-MM-YYYY_HH-MM-SS\nDD-MM-YYYY_HH-MM')
