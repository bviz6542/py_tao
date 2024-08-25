# 일반적인 MST

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, rootX, rootY):
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootY] > rank[rootX]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

v = int(input())
e = int(input())
edges = []
for _ in range(e):
    (a, b, cost) = map(int, input().split())
    edges.append((cost, a-1, b-1))
edges.sort()

parent = [x for x in range(v)]
rank = [1 for _ in range(v)]
ans = 0

for edge in edges:
    (cost, a, b) = edge
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        union(parent, rank, rootA, rootB)
        ans += cost

print(ans)