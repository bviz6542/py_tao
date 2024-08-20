# 한 번 나왔던 문자가 다시 나오면 노 카운트

t = int(input())

ans = 0

for _ in range(t):
    wrong = False
    dic = {}
    prev = ""
    word = list(input())
    for i in word:
        if prev != i and dic.get(i):
            wrong = True
        else:
            dic[i] = 1
            prev = i

    if not wrong:
        ans += 1

print(ans)