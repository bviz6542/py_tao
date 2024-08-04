# 동전 최소 개수 써가면서 액수 채우는 문제

n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

nums.sort

max = 10001
dp = [max] * (k + 1)
dp[0] = 0

for num in nums:
    for i in range(num, k + 1):
        dp[i] = min(dp[i], dp[i-num] + 1)

if dp[k] == max:
    print(-1)
else:
    print(dp[k])