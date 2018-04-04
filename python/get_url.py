#!/usr/bin/python

import sys
from argparse import ArgumentParser as ap
import requests
import json

parser = ap(description='Get an URL and optionally write it to a file')
parser.add_argument('url', help='URL to request')
parser.add_argument('--json', action='store_true', help='Output as JSON. Default is text')
parser.add_argument('--file', '-f', help='Store answer in this file. Default is stdout')

args = parser.parse_args()

r = requests.get(args.url)

if r.status_code != 200:
    print(f"Error: failed to get url: {r.statuscode}")
    sys.exit(1)

if args.json:
    try:
        # pretty printing :-)
        res = json.dumps(r.json(),sort_keys=True,
                         indent=2, separators=(',', ': '))
    except json.decoder.JSONDecodeError:
        print("Invalid JSON")
        sys.exit(1)
else:
    res = r.text

if args.file:
    try:
        f = open(args.file,'w')
    except OSError as e:
        print(f'Error opening {args.file}. {e}')
    else:
        f.writelines(str(res))
else:
    print(res)
