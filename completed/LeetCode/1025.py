# 번갈아 가며 수 바꿔가는 게임

from typing import List

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1: return False
        elif n == 2: return True
        
        acc = [False for _ in range(n+1)]
        acc[1] = False
        acc[2] = True
        
        for i in range(3, n+1):
            devisors = Solution.find_devisors(i)
            
            acc[i] = False
            for d in devisors:
                if not acc[i - d]:
                    acc[i] = True
                    break
        
        return acc[n]
    
    @staticmethod
    def find_devisors(n: int) -> List[int]:
        div = []
        for i in range(1, n):
            if n % i == 0:
                div.append(i)
        return div
    
# sol = Solution()
# print(sol.divisorGame(4))