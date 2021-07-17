import argparse

from gunicorn_log_parser import parse_to_datetime, read_log


def parse_args() -> argparse.Namespace:
    args_parser = argparse.ArgumentParser(description="Gunicorn log parser")
    args_parser.add_argument(
        "-f",
        "--From",
        type=parse_to_datetime,
        help="Date from which the logs will be taken",
    )
    args_parser.add_argument(
        "-t",
        "--To",
        type=parse_to_datetime,
        help="Date to which the logs will be taken",
    )
    args_parser.add_argument("logfile", type=str, help="Path to log file")

    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    read_log(args.logfile, args.From, args.To)
