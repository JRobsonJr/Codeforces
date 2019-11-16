# 1080B: Margarite and the best present

q = int(raw_input())

for l in xrange(q):
    l, r = map(int, raw_input().split())
    if l % 2 == 0:
        if r % 2 == 0:
            print (l + r) / 2
        else:
            print (l - r - 1) / 2
    else:
        if r % 2 == 0:
            print (r - l + 1) / 2
        else:
            print -(l + r) / 2