# 797C: Minimal string

def find_min(count):
    for i in range(26):
        if count[i] > 0:
            return i
    return -1

def calc_pos(letter):
    return ord(letter) - ord('a')

s = input()
count = [0 for i in range(26)]
for c in s:
    count[calc_pos(c)] += 1
t = []
u = ''

for i in range(len(s)):
    t.append(s[i])
    count[calc_pos(s[i])] -= 1
    while t and find_min(count) != -1 and calc_pos(t[-1]) <= find_min(count):
        u += t.pop()

while len(t) > 0:
    u += t.pop() 

print(u)