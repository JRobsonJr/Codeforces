# 727D: T-Shirts Distribution

def solve(n, sizes, allocation, demands):
    for i in range(n):
        curr = input()
        if len(curr.split(',')) == 1:
            if sizes[curr] > 0:
                sizes[curr] -= 1
                allocation[i] = curr
            else:
                return False
        else:
            demands[curr].append(i)

    for demand, people in demands.items():
        poss_1, poss_2 = demand.split(',')
        for i in range(len(people)):
            if sizes[poss_1] > 0:
                sizes[poss_1] -= 1
                allocation[people[i]] = poss_1
            elif sizes[poss_2] > 0:
                sizes[poss_2] -= 1
                allocation[people[i]] = poss_2
            else:
                return False
    return True

s, m, l, xl, xxl, xxxl = map(int, input().split())
n = int(input())

sizes = { 'S': s, 'M': m, 'L': l, 'XL': xl, 'XXL': xxl, 'XXXL': xxxl }
allocation = ['' for _ in range(n)]
demands = { 'S,M': [], 'M,L': [], 'L,XL': [], 'XL,XXL': [], 'XXL,XXXL': [] }

if not solve(n, sizes, allocation, demands):
    print('NO')
else:
    print('YES')
    for a in allocation:
        print(a)