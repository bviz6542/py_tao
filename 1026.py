number = list(map(int, input().split()))
a__list = list(map(int, input().split()))
b__list = list(map(int, input().split()))

a__list.sort()
b__list.sort(reverse=True)

sum = 0

for i in range(0, number[0]):
    sum += a__list[i] * b__list[i]

print(sum)