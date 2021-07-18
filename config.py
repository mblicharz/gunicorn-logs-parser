from gunicorn_log_parser.statistics import RequestsCount
from gunicorn_log_parser.statistics import AverageSizeSuccessfulResponses
from gunicorn_log_parser.statistics import ResponsesCount
from gunicorn_log_parser.statistics import RequestsPerSecond

log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

statistics = {
    'requests_count': {
        'active': True,
        'class': RequestsCount,
        'placeholder': 'req_count'
    },
    'responses_count': {
        'active': True,
        'class': ResponsesCount,
        'placeholder': 'res_count'
    },
    'requests_per_second': {
        'active': True,
        'class': RequestsPerSecond,
        'placeholder': 'req_per_sec'
    },
    'average_size_successful_requests': {
        'active': True,
        'class': AverageSizeSuccessfulResponses,
        'placeholder': 'avg_size_2xx_resp'
    }
}

output_template = '''
Requests: {req_count}
Requests per second: {req_per_sec}
Responses: {res_count}
Average size of 2xx responses: {avg_size_2xx_resp}
'''
