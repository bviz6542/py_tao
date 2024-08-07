# 빗물이 얼마나 고일까

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

if len(blocks) <= 2:
    print(0)

elif len(blocks) == 3:
    if blocks[1] < blocks[0] and blocks[1] < blocks[2]:
        print(min(blocks[0], blocks[2]) - blocks[1])
    else:
        print(0)

else:
    sum = 0
    for i in range(1, len(blocks) - 1):
        left_max = max(blocks[:i+1])
        right_max = max(blocks[i:])
        min_of_max = min(left_max, right_max)
        if blocks[i] < min_of_max:
            sum += min_of_max - blocks[i]
    print(sum)