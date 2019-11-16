# 1146B: Hate "A"

def remove_a(string, length):
    new = ''
    for i in xrange(length):
        if string[i] != 'a':
            new += string[i]
    return new

def solve(string):
    length = len(string)
    last_a = -1

    for i in xrange(len(string) - 1, -1, -1):
        if string[i] == 'a':
            last_a = i
            break

    if last_a == -1:
        if length % 2 == 1:
            return ':('
        else:
            if string[:length / 2] == string[length / 2:]:
                return string[:length / 2]
            else:
                return ':('
    else:
        original_s = string[:last_a + 1]
        s = remove_a(original_s, last_a + 1)
        s_line = string[last_a + 1:]
        left = 0
        while len(s) < len(s_line) - left:
            original_s += s_line[left]
            s += s_line[left]
            left += 1

        if len(s) == len(s_line) - left and s == s_line[left:]:
            return original_s
        else:
            return ':('

string = raw_input()
print(solve(string))