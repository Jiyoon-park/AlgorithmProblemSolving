def DFS(n, summ):
    global minn
    if n > minn:
        return
    if summ > M:
        return
    elif summ == M:
        if minn > n:
            minn = n
    else:
        for i in range(N):
            DFS(n+1, summ+type[i])

N= int(input())
type = list(map(int, input().split()))
type.sort(reverse=True)
minn = 2**53-1
M = int(input())

DFS(0, 0)
print(minn)