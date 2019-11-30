# 676A: Nicholas and Permutation

n = int(raw_input())
arr = map(int, raw_input().split())

pos_1 = arr.index(1)
pos_n = arr.index(n)

# mover 1 para ponta esquerda, mover n para ponta esquerda, mover 1 para ponta direita, mover n para ponta direita

if pos_1 == 0 or pos_1 == n - 1 or pos_n == 0 or pos_n == n - 1:
    print n - 1
else:
    print(max(abs(n - pos_n - 1), abs(n - pos_1 - 1), pos_1 - 0, pos_n - 0))