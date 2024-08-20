# 1부터 N까지 오름차순이고 M 자리인 애들 나열

n, m = map(int, input().split())
visited = []

def back_track(depth):
    if depth == m:
        print(" ".join(map(str, visited)))
        return
    for i in range(1, n+1):
        if i not in visited:
            if len(visited) == 0:
                visited.append(i)
                back_track(depth=depth+1)
                visited.pop()
            elif visited[-1] < i:
                visited.append(i)
                back_track(depth=depth+1)
                visited.pop()
            
back_track(depth=0)