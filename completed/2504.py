line = list(input())

stack = []
result = 0
temp = 1
wrong_answer = False

def answer():
    global temp
    global result
    global wrong_answer

    is_asc = True

    for char in line:
        if char == '(':
            stack.append('(')
            temp *= 2
            is_asc = True

        if char == ')':
            if stack and stack.pop() == '(':
                if is_asc:
                    result += temp
                temp = temp / 2
                is_asc = False
            else:
                wrong_answer = True
                return

        if char == '[':
            stack.append('[')
            temp *= 3
            is_asc = True

        if char == ']':
            if stack and stack.pop() == '[':
                if is_asc:
                    result += temp
                temp = temp / 3
                is_asc = False

            else:
                wrong_answer = True
                return

answer()

if stack:
    print(0)
elif wrong_answer:
    print(0)
else:
    print(int(result))