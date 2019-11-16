# 1093A: Dice Rolling

import math

t = int(raw_input())

for i in xrange(t):
    points = int(raw_input())
    print int(math.ceil(points / 7.0))