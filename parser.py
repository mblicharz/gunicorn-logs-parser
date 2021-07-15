import argparse

from log_reader import parse_to_datetime
from log_reader import RequestCounter, ResponseCounter, AverageCounter
from log_reader import LogReader, LineReader

parser = argparse.ArgumentParser(description='parser')

parser.add_argument('-f', '--From', type=parse_to_datetime, help='From date')
parser.add_argument('-t', '--To', type=parse_to_datetime, help='To date')
parser.add_argument('logfile', type=str)

args = parser.parse_args()

log_reader = LogReader(args.logfile, args.From, args.To)

lines_count = 0
request_counter = RequestCounter()
response_counter = ResponseCounter()
avg_counter = AverageCounter()

first_date = None
last_date = None

for line in log_reader:
    lines_count += 1

    try:
        line_reader = LineReader(line)
    except ValueError:
        continue

    response_counter.update({line_reader.status_code: 1})

    if 300 > int(line_reader.status_code) >= 200:
        avg_counter.add(int(line_reader.response_len))

    request_counter.update(1)

print('Parsing results:')

print(f'All records: {lines_count}')

print(f'processed requests: {request_counter.count}')

first_date = log_reader.first_date
last_date = log_reader.last_date
requests_per_sec = request_counter.get_requests_per_second(first_date,
                                                           last_date)
requests_per_sec = ("%.2f" % requests_per_sec)
print(f'requests per sec: {requests_per_sec}')

print(f'responses: {response_counter.get_output()}')

avg_size = ("%.2f" % (avg_counter.average() * 8 / 1024))
print(f'Average size of 2xx responses: {avg_size} Mb')
