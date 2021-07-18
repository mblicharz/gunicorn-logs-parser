from gunicorn_log_parser.statistics import RequestsCount
from gunicorn_log_parser.statistics import ResponsesCount

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
    }
}

output_template = '''
Requests: {req_count}
Responses: {res_count}
'''
