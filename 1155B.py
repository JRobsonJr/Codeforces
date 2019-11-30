# 1155B: Game with Telephone Numbers

n = int(raw_input()) # s eh impar
s = raw_input()

rounds = n - 11
vasya_remain = rounds / 2
petya_remain = rounds / 2

first = ''
i = 0
while first == '':
    if s[i] == '8':
        if petya_remain > 0:
            petya_remain -= 1
            i += 1
        else:
            print 'YES'
            first = '8'
    else:
        if vasya_remain > 0:
            vasya_remain -= 1
            i += 1
        else:
            print 'NO'
            first = s[i]