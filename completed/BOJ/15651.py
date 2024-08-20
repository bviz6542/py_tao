# 1부터 N까지 중복 있이 M 자리 문자열

n, m = map(int, input().split())

visited = []

def back_track(depth):
    if depth == m:
        print(" ".join(map(str, visited)))
        return
    for i in range(1, n+1):
        visited.append(i)
        back_track(depth=depth+1)
        visited.pop()

back_track(0)