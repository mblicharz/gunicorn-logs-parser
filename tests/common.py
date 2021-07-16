log_file_path = './tests/resources/test_logs.log2'
log_file_with_wrong_format_path = './tests/resources/test_logs2.log2'

log_line_with_splitted_output = {
    'output': (
        '172.16.3.14', '-', '01/Dec/2019:11:06:05 +0100',
        'GET /internal/user/38ca8008-fb70-44f0-a356-9bb9192ba15c/agenda/2019-12-01/2019-12-02 HTTP/1.1',
        '200', '720', '-', 'python-requests/2.22.0',
        '276202'),
    'line': '172.16.3.14 - - [01/Dec/2019:11:06:05 +0100] "GET /internal/user/38ca8008-fb70-44f0-a356-9bb9192ba15c/agenda/2019-12-01/2019-12-02 HTTP/1.1" 200 720 "-" "python-requests/2.22.0" 276202'
}


def _count_example_log_file_lines(log_file: str) -> int:
    lines_count = 0
    with open(log_file) as file:
        next(file)
        for _ in file:
            lines_count += 1
    return lines_count


log_file_lines_count = _count_example_log_file_lines(log_file_path)
