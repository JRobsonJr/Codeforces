# 1251A: Yellow Cards

a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

curr_cards = n
curr_cards -= (k1 - 1) * a1 + (k2 - 1) * a2
minimum = 0
if curr_cards > 0:
    minimum = curr_cards

curr_cards = n
remaining_cards = 0
maximum = 0
if k1 > k2:
    k1, k2 = k2, k1
    a1, a2 = a2, a1
remaining_cards += curr_cards % k1 # não vai dar pra usar
curr_cards -= curr_cards % k1 # só pro primeiro cálculo
div = curr_cards / k1
maximum += min(div, a1)
remaining_cards += (div - min(div, a1)) * k1
maximum += remaining_cards // k2

print(minimum, int(maximum))