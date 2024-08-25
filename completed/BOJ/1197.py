# 일반적인 MST

def find(parent, x) -> int:
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b) -> None:
    rootA = parent[a]
    rootB = parent[b]
    if rootA != rootB:
        if rank[a] > rank[b]:
            parent[rootB] = rootA
        elif rank[a] < rank[b]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

v, e = map(int, input().split())
edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a-1, b-1))
edges.sort()

parent = [x for x in range(v)]
rank = [1 for _ in range(v)]
ans = 0

for edge in edges:
    (cost, a, b) = edge
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        ans += cost

print(ans)