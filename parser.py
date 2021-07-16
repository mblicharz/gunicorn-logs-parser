import argparse

from log_reader import parse_to_datetime, read_log


def parse_args() -> argparse.Namespace:
    args_parser = argparse.ArgumentParser(description='parser')
    args_parser.add_argument('-f', '--From', type=parse_to_datetime,
                             help='From date')
    args_parser.add_argument('-t', '--To', type=parse_to_datetime,
                             help='To date')
    args_parser.add_argument('logfile', type=str)

    return args_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    read_log(args.logfile, args.From, args.To)
