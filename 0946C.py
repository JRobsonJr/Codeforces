# 946C: String Transformation

s = list(input())

initial_ord = ord('a')
final_ord = ord('z')
curr_ord = ord('a')
index = 0

while index < len(s):
    if ord(s[index]) <= curr_ord:
        s[index] = chr(curr_ord)
        curr_ord += 1
    index += 1
    if curr_ord == final_ord + 1:
        break

if curr_ord == final_ord + 1:
    print(''.join(s))
else:
    print(-1)