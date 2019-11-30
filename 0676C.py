# 676C: Vasya and String

def try_for_letter(w, letter):
    l = 0
    r = 0
    curr_k = 0
    best = 0
    while r < n:
        if (w[r] != letter):
            curr_k += 1
        if curr_k <= k:
            best = max(best, r - l + 1)
        else:
            while curr_k > k:
                if w[l] != letter:
                    curr_k -= 1
                l += 1
        r += 1
    return best

n, k = map(int, input().split())
w = input()

print(max(try_for_letter(w, 'a'), try_for_letter(w, 'b')))