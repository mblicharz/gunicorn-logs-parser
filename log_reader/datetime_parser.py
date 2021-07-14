from datetime import datetime

VALID_DATE_FORMATS = ['%d-%m-%Y_%H-%M-%S', '%d-%m-%Y_%H-%M']


def parse_to_datetime(datetime_str: str) -> datetime:
    dt = None

    for date_format in VALID_DATE_FORMATS:
        try:
            dt = datetime.strptime(datetime_str, date_format)
        except ValueError:
            pass
        else:
            break
    else:
        _print_error()

    return dt


def _print_error():
    print(f'Invalid date format. Valid formats:\n'
          f'DD-MM-YYYY_HH-MM-SS\nDD-MM-YYYY_HH-MM')
