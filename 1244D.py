# 1244D: Paint the Tree

def is_possible(adj, n):
    for i in range(n):
        if len(adj[i]) >= 3:
            return False
    return True

def color_pattern(adj, n):
    stack = []
    for i in range(n): # Encontrar um nó folha
        if len(adj[i]) == 1:
            stack.append(i)
            break
    dist = [-1 for i in range(n)]
    dist[i] = 0
    while stack:
        curr = stack.pop()
        for n in adj[curr]:
            if dist[n] == -1:
                stack.append(n)
                dist[n] = (dist[curr] + 1) % 3
    return dist

def try_for_colors(n, adj, costs, pattern, seq):
    colors = []
    cost = 0
    for i in range(n):
        cost += costs[seq[pattern[i]] - 1][i]
        colors.append(seq[pattern[i]])
    return cost, colors

n = int(input())
c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
costs = [c1, c2, c3]

adj = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adj[u].append(v)
    adj[v].append(u)

if is_possible(adj, n):
    pattern = color_pattern(adj, n)
    min_cost, min_colors = try_for_colors(n, adj, costs, pattern, [1, 2, 3])
    poss = [[1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    for p in poss:
        cost, colors = try_for_colors(n, adj, costs, pattern, p)
        if cost < min_cost:
            min_cost = cost
            min_colors = colors
    print(min_cost)
    print(' '.join(map(str, min_colors)))
else:
    print(-1)