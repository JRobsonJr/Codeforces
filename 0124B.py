# 124B: Permutations

import math
import itertools
n, k = map(int, input().split())

numbers = []
for i in range(n):
    numbers.append(input())

permutations = []
for number in numbers:
    curr = [int(''.join(perm)) for perm in itertools.permutations(number)]
    permutations.append(curr)

possibilities = [[] for i in range(math.factorial(k))]
for i in range(n):
    for j in range(math.factorial(k)):
        possibilities[j].append(permutations[i][j])

minimum = 99999999
for poss in possibilities:
    minimum = min(max(poss) - min(poss), minimum)

print(minimum)