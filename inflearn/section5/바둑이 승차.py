def dfs(summ):
    global maxV
    if summ > maxV:
        if summ > C:
            return
        maxV = summ
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(summ+dogs[i])
            used[i] = 0

C, N = map(int, input().split())
dogs = []
for _ in range(N):
    dogs.append(int(input()))
maxV = 0
used = [0]*N

dfs(0)
print(maxV)