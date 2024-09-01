# 지정된 점에서의 최단 거리래

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        q = [(0, k)]
        ans = [INF] * (n+1)
        ans[0] = 0
        ans[k] = 0
        graph = [[] for _ in range(n+1)]
        for edge in times:
            a, b, time = edge
            graph[a].append((b, time))

        while q:
            time, node  = heapq.heappop(q)
            for nei_node, nei_time in graph[node]:
                if ans[node] + nei_time < ans[nei_node]:
                    ans[nei_node] = ans[node] + nei_time
                    heapq.heappush(q, (ans[nei_node], nei_node))

        if max(ans) == INF:
            return -1
        else:
            return max(ans)


# sol = Solution()
# print(sol.networkDelayTime(times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2))