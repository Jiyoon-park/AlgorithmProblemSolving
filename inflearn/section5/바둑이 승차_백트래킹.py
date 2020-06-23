def DFS(L, summ, tsumm):
    global result
    if summ + (total-tsumm) < result:
        return
    if summ > C:
        return
    if L == N:
        if summ > result:
            result = summ
    else:
        DFS(L + 1, summ + dogs[L], tsumm + dogs[L])
        DFS(L + 1, summ, tsumm + dogs[L])

C, N = map(int, input().split())
dogs = []
for _ in range(N):
    dogs.append(int(input()))
result = 0
total = sum(dogs)
DFS(0, 0, 0)
print(result)