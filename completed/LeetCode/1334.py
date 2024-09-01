# 도시 간 이동에 상한선이 있음. 제일 연결 적은 애 찾으셈.

from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans = []
        def dijkstra(n: int, edges: List[List[int]], start_node: int, distanceThreshold: int, min_neighbor: int, ans: List[int]):
            INF = int(1e9)
            distance = [INF] * n
            graph = [[] for _ in range(n)]
            for edge in edges:
                a, b, dist = edge
                graph[a].append((dist, b))
                graph[b].append((dist, a))
            q = [(0, start_node)]
            distance[start_node] = 0

            while q:
                dist, node = heapq.heappop(q)
                for (nei_dist, nei_node) in graph[node]:
                    new_dist = nei_dist + distance[node]
                    if new_dist > distanceThreshold:
                        continue
                    if new_dist < distance[nei_node]:
                        distance[nei_node] = new_dist
                        heapq.heappush(q, (new_dist, nei_node))
        
            count = 0
            for d in distance:
                if d != INF:
                    count += 1
            
            ans.append([count, start_node])

        for node in range(n):
            dijkstra(n, edges=edges, start_node=node, distanceThreshold=distanceThreshold, min_neighbor=0, ans=ans)

        ans.sort(key=lambda x: (x[0], -x[1]))

        return ans[0][1]

# sol = Solution()
# print(sol.findTheCity(n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=4))