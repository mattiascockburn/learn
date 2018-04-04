from math import pi
import os

c = int(os.getenv('DIGITS') or 10)
print(round(pi, c))
