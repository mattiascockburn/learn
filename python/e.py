#!/usr/bin/python
import argparse
import sys

parser =argparse.ArgumentParser(description='some demo program')

parser.add_argument('file_name', help='the file to work with')
parser.add_argument('line_number', type=int,help='the line number to print')

args = parser.parse_args()

try:
    lines = open(args.file_name).readlines()
    line = lines[args.line_number -1]
except OSError as e:
    print(f"Error: {e}")
    sys.exit(1)
except IndexError:
    print('Line does not exist')
    sys.exit(1)
else:
    print(line)

