from collections import deque

def DFS(graph, start_node):
    visited = []
    stack = [start_node]
    while(stack):
        cur = stack.pop()
        if cur not in visited:
            visited.append(cur)
            stack += sorted(list(graph[cur] - set(visited)), reverse = True)
    return visited

def BFS(graph, start_node):
    visited = []
    queue = deque([start_node])
    while(queue):
        cur = queue.popleft()
        if cur not in visited:
            visited.append(cur)
            queue += sorted(list(graph[cur] - set(visited)))
    return visited

node_num, edge_num, start_node = map(int, input().split())
graph = dict()
for i in range(1, node_num+1):
    graph[i] = set()

for _ in range(1, edge_num+1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    # 없애는 건 discard

def print_list(input_list):
    printing = ''
    for i in input_list:
        printing += str(i) + ' '
    printing = printing[:-1]
    return printing

print(print_list(DFS(graph, start_node)))
print(print_list(BFS(graph, start_node)))
