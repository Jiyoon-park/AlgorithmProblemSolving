N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

result = []
maxV = summ1 = summ2 = 0
for i in range(N):
    summ = 0
    for j in range(N):
        summ += nums[i][j]
        if i == j:
            summ1 += nums[i][j]
        elif i + j == N:
            summ2 += nums[i][j]
    if maxV < summ:
        maxV = summ
if maxV < summ1:
    maxV = summ1
if maxV < summ2:
    maxV = summ2

for j in range(N):
    summ = 0
    for i in range(N):
        summ += nums[i][j]
    if maxV < summ:
        maxV = summ

print(maxV)

