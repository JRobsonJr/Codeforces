# 816A: Karen and Morning

def tomin(h):
    h, m = h.split(':')
    return int(h) * 60 + int(m)
def diff(h1, h2):
    return tomin(h1) - tomin(h2)

pals = []
for i in xrange(24):
    istr = str(i).zfill(2)
    rev = istr[::-1]
    if int(rev) <= 59:
        pals.append(istr + ':' + rev)

sleep = raw_input()

if sleep == '00:00':
    print 0
elif sleep[0] + sleep[1] == '23' and int(sleep[3] + sleep[4]) > 32:
    print 60 - int(sleep[3] + sleep[4])
else:
    for pal in pals[1:]:
        if tomin(pal) >= tomin(sleep):
            print(diff(pal, sleep))
            break