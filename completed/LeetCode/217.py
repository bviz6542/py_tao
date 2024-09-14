from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for e in nums:
            if dic.get(str(e)):
                return True
            dic[str(e)] = 1
        return False

sol = Solution()
a = sol.containsDuplicate([1,4,3,2])
print(a)