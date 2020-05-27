sticks = input()

result = cnt = 0
for i in range(len(sticks)-1):
    if sticks[i] == '(':
        if sticks[i+1] == ')':
            if cnt == 0:
                continue
            else:
                result += cnt
        elif sticks[i+1] == '(':
            cnt += 1
    elif sticks[i] == ')':
        if sticks[i+1] == ')':
            result += 1
            cnt -= 1
        elif sticks[i+1] == '(':
            continue
print(result)


