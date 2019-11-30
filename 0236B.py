# 236B: Easy Number Challenge

MAX_N = 1000001
MOD = 2 ** 30

d = [1 for i in range(MAX_N)]

for i in range(2, MAX_N):
	for j in range(i, MAX_N, i):
	    d[j] += 1

a, b, c = map(int, input().split())
res = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            res += d[i * j * k]
            res %= MOD

print(res % MOD)