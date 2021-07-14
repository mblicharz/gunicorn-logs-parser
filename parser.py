import argparse

from datetime_type import datetime_T

parser = argparse.ArgumentParser(description='parser')

parser.add_argument('-f', '--From', type=datetime_T, help='From date')
parser.add_argument('-t', '--To', type=datetime_T, help='To date')
parser.add_argument('logfile', type=str)

args = parser.parse_args()
