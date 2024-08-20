from collections import deque

n = int(input())
arr = deque()
arr.extend(list(range(n)))

while len(arr) > 1:
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()

print(arr[0]+1)