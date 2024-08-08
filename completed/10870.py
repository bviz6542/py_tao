# 피보나치 수

n = int(input())

a_1 = 1
a_2 = 1
a_3 = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)

for i in range(3, n + 1):
    a_3 = a_1 + a_2
    a_1 = a_2
    a_2 = a_3
    if i == n:
        print(a_3)