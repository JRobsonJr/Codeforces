# 121A: Lucky Sum

def generate_lucky_numbers():
    lucky_digits = ['4', '7']
    lucky_numbers = []
    curr_appenders = [4, 7]
    for _ in range(10):
        lucky_numbers.extend(curr_appenders)
        curr_appenders = [int(ld + str(ca)) for ld in lucky_digits for ca in curr_appenders]
    return lucky_numbers

def get_next_lucky_number_index(lucky_numbers, query):
    index = 0
    while lucky_numbers[index] < query:
        index += 1
    return index

def solve(l, r):
    lucky_numbers = generate_lucky_numbers()
    lucky_pointer = get_next_lucky_number_index(lucky_numbers, l)
    if get_next_lucky_number_index(lucky_numbers, r) == lucky_pointer:
        return lucky_numbers[lucky_pointer] * (r - l + 1)
    else:
        lucky_pointer = get_next_lucky_number_index(lucky_numbers, l)
        lucky_sum = lucky_numbers[lucky_pointer] * (lucky_numbers[lucky_pointer] - l + 1)
        lucky_pointer += 1
        while lucky_numbers[lucky_pointer] < r:
            lucky_sum += lucky_numbers[lucky_pointer] * (min(lucky_numbers[lucky_pointer], r) - lucky_numbers[lucky_pointer - 1])
            lucky_pointer += 1
    
        lucky_sum += lucky_numbers[lucky_pointer] * (r - lucky_numbers[lucky_pointer - 1])
        
        return lucky_sum

l, r = map(int, input().split())
print(solve(l, r))