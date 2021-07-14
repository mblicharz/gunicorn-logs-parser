import argparse

from datetime_type import datetime_T
from log_reader import LogReader

parser = argparse.ArgumentParser(description='parser')

parser.add_argument('-f', '--From', type=datetime_T, help='From date')
parser.add_argument('-t', '--To', type=datetime_T, help='To date')
parser.add_argument('logfile', type=str)

args = parser.parse_args()

log_reader = LogReader(args.logfile, args.From, args.To)

counter = 0

for lines in log_reader:
    counter += 1

print(f'requests: {counter}')
