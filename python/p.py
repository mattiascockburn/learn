#!/usr/bin/python
import os
import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('port_number', type=int)
args = parser.parse_args()

c = ['lsof','-n',f'-i4TCP:{args.port_number}']
try:
    p = subprocess.run(c, check=True, stdout=subprocess.PIPE).stdout
except subprocess.CalledProcessError:
    print(f'No program listening on {args.port_number}')
    sys.exit(1)
pid = int(bytes.decode(p).split()[10])
os.kill(pid,9)
