# Gunicorn logs parser
Script for parsing gunicorn log to get some statistics from it.

### Log format
The log format given below is a default one, and stores **all supported** identifiers.
The format can be changed in _config.py_.
```
%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s
```
For extending supported identifiers, read more [here](#log-format-identifiers).
### Statistics types
- requests count 
- requests per second
- amount of different status codes
- average size of 2xx responses

### Installation
No installation needed. There is no dependencies to fulfill. 
However **pytest** is required for tests execution.

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

#### Output example
```
All lines: 67721
Requests: 67721
Requests per second: 0.72
Responses: (200: 65689, 404: 2032)
avg size of 2xx responses: 6.11 Mb
```

## Development
#### Log format identifiers
If given above identifiers are not enough, you can add another in _log_line.py_.
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
