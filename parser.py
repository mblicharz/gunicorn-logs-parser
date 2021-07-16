import argparse

from log_reader import parse_to_datetime
from log_reader import RequestCounter, ResponseCounter, AverageCounter
from log_reader import LogReader, LogLine


def is_status_code_2xx(status_code: int) -> bool:
    return 300 > status_code >= 200


args_parser = argparse.ArgumentParser(description='parser')

args_parser.add_argument('-f', '--From', type=parse_to_datetime,
                         help='From date')
args_parser.add_argument('-t', '--To', type=parse_to_datetime, help='To date')
args_parser.add_argument('logfile', type=str)

args = args_parser.parse_args()

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
        line_reader = LogLine(line)
    except ValueError:
        # TODO: Add warning about invalid log line
        continue

    response_counter.update({line_reader.status_code: 1})

    if is_status_code_2xx(int(line_reader.status_code)):
        avg_counter.add(int(line_reader.response_len))

    request_counter.update(1)

print('Parsing results:')

print(f'All records: {lines_count}')

print(f'processed requests: {request_counter.count}')

first_date = log_reader.first_date
last_date = log_reader.last_date
requests_per_sec = request_counter.get_requests_per_second(
    first_date,
    last_date
)
requests_per_sec = ("%.2f" % requests_per_sec)
print(f'requests per sec: {requests_per_sec}')

print(f'responses: {response_counter.get_output()}')

# TODO: Move to external file
avg_size = ("%.2f" % (avg_counter.average() * 8 / 1024))
print(f'Average size of 2xx responses: {avg_size} Mb')

# TODO: Add main
