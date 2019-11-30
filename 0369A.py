# 369A: Valera and Plates

n, m, k = map(int, raw_input().split())
a = map(int, raw_input().split())

count = 0
for ai in a:
    if ai == 1:
        if m == 0:
            count += 1
        else:
            m -= 1
    else:
        if k == 0:
            if m == 0:
                count += 1
            else:
                m -= 1
        else:
            k -= 1

print count