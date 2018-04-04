#!/usr/bin/python
try:
  f = open(input('file: '), 'w')
except OSError:
    print('something happened')
while True:
    l = input('=> ')
    if l == '':
        break
    f.write(l + '\n')
f.close()
