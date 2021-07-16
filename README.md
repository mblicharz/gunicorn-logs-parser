# Gunicorn logs parser
Script for parsing gunicorn log to get some statistics from it.

### Log format
The only supported format at this moment is:
```
%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s
```

### Statistics types
- requests count 
- requests per second
- amount of different status codes
- average size of 2xx responses

### Installation
No installation needed. There is any dependiencies to fullfill. However **pytest** is required for tests execution.

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
