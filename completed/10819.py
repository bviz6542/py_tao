# 이웃한 숫자 간 차이 합의 최대
# 이미 방문한 값들 구별 되게 해야 함

length = int(input())
nums = list(map(int, input().split()))

max = -1
def back_track(index_visited):
    global max

    if len(index_visited) == len(nums):
        temp = 0
        for i in range(1, len(index_visited)):
            temp += abs(nums[index_visited[i]] - nums[index_visited[i-1]])
        if temp > max:
            max = temp
        return

    for index in range(len(nums)):
        if index not in index_visited:
            index_visited.append(index)
            back_track(index_visited)
            index_visited.pop()
    
back_track([])
print(max)