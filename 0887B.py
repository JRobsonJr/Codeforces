# 887B: Cubes for Masha

n = int(input())
cubes = [set() for i in range(10)]

for i in range(n):
    for n in sorted(list(map(int, input().split()))):
        cubes[n].add(i)

# Tentar só até 99; 1 até 99 já é sempre impossível.
# Justificativa: são necessárias 20 dígitos para fazer
# 11, 22, ..., 99 e em três dados só há 18 faces.

for curr in range(1, 100):
    str_curr = str(curr)
    if len(str_curr) == 1:
        if len(cubes[curr]) == 0:
            print(curr - 1)
            break
    else:
        d1 = int(str_curr[0])
        d2 = int(str_curr[1])
        if len(cubes[d2]) == 0 or len(cubes[d1].union(cubes[d2])) == 1:
            print(curr - 1)
            break