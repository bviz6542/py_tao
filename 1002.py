# 터렛으로 위치 확인

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    else:
        distance_square = ((x1 - x2)**2 + (y1 - y2)**2)
        r_sum_square = (r1 + r2) ** 2
        if distance_square == r_sum_square :
            print(1)
        elif distance_square > r_sum_square:
            print(0)
        elif distance_square == (r1 - r2)**2:
            print(1)
        elif distance_square < (r1 - r2)**2:
            print(0)
        else:
            print(2)