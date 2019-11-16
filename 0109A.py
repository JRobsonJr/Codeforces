# 109A: Lucky Sum of Digits

n = int(raw_input())
x = 0
y = 0

while 4 * x <= n:
    if (n - 4 * x) % 7 == 0:
        y = (n - 4 * x) / 7
        break
    else: 
        x += 1

if x * 4 + y * 7 == n:
    print '4' * x + '7' * y
else:
    print -1