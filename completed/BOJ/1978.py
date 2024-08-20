# 소수 몇 개인지 찾아봐

import math

n = int(input())
nums = list(map(int, input().split()))

max_num = 1000

reverse_ans = 0
for i in nums:
    if i == 1:
        reverse_ans += 1

    for j in range(2, i):
        if i % j == 0:
            reverse_ans += 1
            break

print(len(nums) - reverse_ans)

