#!/usr/bin/python
import crypt
import sys

try:
    print(crypt.crypt(sys.argv[1], crypt.mksalt(crypt.METHOD_SHA512)))
except IndexError:
    print('You need to supply a password')

