# 계단 하나 또는 두개씩 오르기

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        acc = [0 for _ in range(n)]
        acc[0] = cost[0]
        acc[1] = cost[1]
        for i in range(2, n):
            acc[i] = min(acc[i-1], acc[i-2]) + cost[i]
            
        return min(acc[n-1], acc[n-2])

# sol = Solution()
# print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))