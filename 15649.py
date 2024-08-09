# 1부터 N까지의 수를 M개 나열

n, m = map(int, input().split())
visited = []

def back_track():
    if len(visited) == m:
        print(" ".join(map(str, visited)))
        return
    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            back_track()
            visited.pop()

back_track()        
