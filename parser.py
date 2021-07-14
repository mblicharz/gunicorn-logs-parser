import argparse

from log_reader import parse_to_datetime
from log_reader import LogReader

parser = argparse.ArgumentParser(description='parser')

parser.add_argument('-f', '--From', type=parse_to_datetime, help='From date')
parser.add_argument('-t', '--To', type=parse_to_datetime, help='To date')
parser.add_argument('logfile', type=str)

args = parser.parse_args()

log_reader = LogReader(args.logfile, args.From, args.To)

counter = 0

for lines in log_reader:
    print(lines)
    counter += 1

print(f'requests: {counter}')
