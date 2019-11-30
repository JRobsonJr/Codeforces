# 633A: Ebony and Ivory

a, b, c = map(int, raw_input().split())

def solve(a, b, c):
    if a == 1 or b == 1 or c % a == 0 or c % b == 0:
        return True
    max_a = c / a
    for i in xrange(1, max_a + 1):
        if (c - i * a) % b == 0:
            return True
    return False

print 'Yes' if solve(a, b, c) else 'No'