# 파스칼 삼각형

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        graph = [[1] * (rowIndex+1) for _ in range(rowIndex+1)]

        for i in range(rowIndex):
            for j in range(i):
                graph[i+1][j+1] = graph[i][j+1] + graph[i][j]
            
        return graph[rowIndex]
        
# sol = Solution()
# print(sol.getRow(8))