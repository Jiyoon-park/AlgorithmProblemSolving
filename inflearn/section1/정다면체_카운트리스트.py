N, M = map(int, input().split())
cnt = [0]*(N+M+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i + j] += 1

# 가장 높은 확률 찾기
maxV = 0
for i in range(len(cnt)):
    if maxV < cnt[i]:
        maxV = cnt[i]
# 가장 높은 확률의 수 찾기
for i in range(len(cnt)):
    if cnt[i] == maxV:
        print(i, end=" ")

