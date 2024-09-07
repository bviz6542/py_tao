# 그냥 피보나치

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        
        arr = [0 for _ in range(n+1)]
        arr[1] = 1
        for i in range(n - 1):
            arr[i + 2] = arr[i] + arr[i + 1]
        return arr[n]
    
# sol = Solution()
# for i in range(11):
#     print(sol.fib(i))        