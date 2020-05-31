essential = input()
N = int(input())
result = []
for _ in range(N):
    curr = input()
    temp = 'x'
    for i in range(len(curr)):
        if curr[i] in essential and temp[-1] != curr[i]:
            temp += curr[i]
    if temp[1:len(essential)+1] == essential:
        result.append('YES')
    else:
        result.append('NO')
for i in range(len(result)):
    print('#{} {}'.format(i+1, result[i]))