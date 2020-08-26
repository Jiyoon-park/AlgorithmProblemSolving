def DFS(v, summ):
    global maxx
    if summ > C:
        return
    if v >= N:
        if maxx < summ:
            maxx = summ
    else:
        DFS(v+1, summ+dogs[v])
        DFS(v+1, summ)


C, N = map(int, input().split())
dogs = []
maxx = 0
for _ in range(N):
    dogs.append(int(input()))

DFS(0, 0)
print(maxx)