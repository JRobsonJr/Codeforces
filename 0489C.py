# 489C: Given Length and Sum of Digits...

m, s = map(int, input().split())

def biggest_number(length, sum_digits):
    if (length > 1 and sum_digits == 0) or length * 9 < sum_digits:
        return -1
    number = ''
    curr_digit = 0
    remaining_sum = sum_digits
    while remaining_sum > 0:
        number += str(min(remaining_sum, 9))
        remaining_sum -= min(remaining_sum, 9)
        curr_digit += 1
    if len(number) > length or sum([int(digit) for digit in number]) != sum_digits:
        return -1
    return number + '0' * (length - len(number))

def smallest_number(length, sum_digits):
    if (length > 1 and sum_digits == 0) or length * 9 < sum_digits:
        return -1
    if length == 1 and sum_digits == 0:
        return 0
    number = [0 for i in range(length)]
    curr_digit = length - 1
    remaining_sum = sum_digits - 1
    while remaining_sum > 0 and curr_digit >= 0:
        number[curr_digit] = min(remaining_sum, 9)
        remaining_sum -= min(remaining_sum, 9)
        curr_digit -= 1
    if number[0] < 9 and sum(number) == sum_digits - 1:
        number[0] += 1
        return ''.join(map(str, number))
    else:
        return -1

print(smallest_number(m, s), biggest_number(m, s))