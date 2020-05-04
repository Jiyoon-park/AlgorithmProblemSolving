N = int(input())
problems = list(input().split())

score = 0
temp = 0
for i in range(N):
    if problems[i] == '1':
        temp += 1
        score += temp
    else:
        temp = 0
print(score)
