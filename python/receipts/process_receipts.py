#!/usr/bin/python
import os
import glob
import json
import shutil

d='./processed'
try:
    os.mkdir(d)
except FileExistsError:
    print('flupp')

subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    dest = path.replace('./new', d)
    shutil.move(path, dest)
    print(f"moved '{path}' to '{dest}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")

