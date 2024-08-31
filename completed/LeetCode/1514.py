# edge마다 확률이 적혀있다. 최대 확률 구하자.

from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distance = [0.0] * n
        distance[start_node] = 1.0
        q = [(-1.0, start_node)]
        graph = [[] for _ in range(n)]
        
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        while q:
            prob, node = heapq.heappop(q)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for next_node, weight in graph[node]:
                new_prob = prob * weight
                if new_prob > distance[next_node]:
                    distance[next_node] = new_prob
                    heapq.heappush(q, (-new_prob, next_node))
        
        return distance[end_node]

# sol = Solution()
# print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))