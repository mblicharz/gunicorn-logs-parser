def get_log_file():
    return './tests/test_logs.log2'


def get_log_line_with_grouped_output():
    return {
        'output': (
            '172.16.3.14', '-', '01/Dec/2019:11:06:05 +0100',
            'GET /internal/user/38ca8008-fb70-44f0-a356-9bb9192ba15c/agenda/2019-12-01/2019-12-02 HTTP/1.1',
            '200', '720', '-', 'python-requests/2.22.0',
            '276202'),
        'line': '172.16.3.14 - - [01/Dec/2019:11:06:05 +0100] "GET /internal/user/38ca8008-fb70-44f0-a356-9bb9192ba15c/agenda/2019-12-01/2019-12-02 HTTP/1.1" 200 720 "-" "python-requests/2.22.0" 276202'
    }
