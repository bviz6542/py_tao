N = list(map(int, input().split()))[0]

sum = 0
i = 0
while(1):
    i += 1
    sum += i
    if N>sum:
        continue
    elif N==sum:
        print(i)
        break
    else:
        print(i-1)
        break