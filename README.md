# Gunicorn logs parser
Parser gunicorn log to get some statistics from it.

### Installation
No installation needed. There is no dependencies to fulfill. 
However **pytest** is required for tests execution.

### Configuration
- _log_format_ - Format containing identifiers provided by [gunicorn].
- _statistics_ - Configs for all statistics, read more [here](#adding-new-statistic-type).
- _output_template_ - Template for the output. You can use placeholders set in statistics config.

### Usage
```
python parser.py [-h] [-f FROM] [-t TO] logfile
```

#### Arguments
```
positional arguments:
  logfile               Path to log file

optional arguments:
  -h, --help            show this help message and exit
  -f FROM, --From FROM  Date from which the logs will be taken
  -t TO, --To TO        Date to which the logs will be taken
```

#### Date format
Allowed formats are:
- DD-MM-YYYY_HH-MM-SS
- DD-MM-YYYY_HH-MM

### Statistics types
- requests count 
- requests per second
- amount of different status codes
- average size of 2xx responses

#### Output example
```
Requests: 99998
Requests per second: 1.07/sec
Responses: (200: 96204, 404: 3794)
Average size of 2xx responses: 0.01 Mb
```

## Development
#### Log format identifiers
You can add new identifier in _[log_line.py]_.
```python
FORMAT_IDENTIFIERS_REGEX = {
    "%(h)s": r'"?([(\d\.)]+)"?',
    "%(l)s": r'"?-"?',
    "%(u)s": r'"?(.*?)"?',
    "%(t)s": r'"?\[(.*?)\]"?',
    "%(r)s": r'"?(.*?)"?',
    "%(s)s": r'"?(\d+)"?',
    "%(b)s": r'"?(\d+)"?',
    "%(f)s": r'"?(.*?)"?',
    "%(a)s": r'"?(.*?)"?',
    "%(D)s": r'"?(\d+)"?',
}

FORMAT_IDENTIFIERS_ATTRIBUTES = {
    "%(h)s": "remote_address",
    "%(u)s": "user_name",
    "%(t)s": "date",
    "%(r)s": "status_line",
    "%(s)s": "status_code",
    "%(b)s": "response_len",
    "%(f)s": "referer",
    "%(a)s": "user_agent",
    "%(D)s": "time",
}
```
To add new identifier, you have to prepare regex, and name of attribute, where your new identifier will be stored in the object.

#### Adding new statistic type
To create your own class for your statistic, you should inherit class _[AbstractStatistic]_, which provides two methods:
- _update()_ - collect and store data from single LogLine object
- _get_result_repr()_ - returns string representation of statistic

Add your new statistic in _config.py_ file into **statistics** section as below:
```python
'requests_count': { # Name of your statistics
        'active': True, # If active, it will be taken into account during calculations
        'class': RequestsCount, # Put here your new class of your statistics
        'placeholder': 'req_count' # Placeholder is used in output template
    }
```

[gunicorn]: <https://docs.gunicorn.org/en/stable/settings.html#access-log-format>
[log_line.py]: <https://github.com/mblicharz/gunicorn-logs-parser/blob/master/gunicorn_log_parser/log_line.py>
[AbstractStatistic]: <https://github.com/mblicharz/gunicorn-logs-parser/blob/master/gunicorn_log_parser/statistics/abstract_statistic.py>
