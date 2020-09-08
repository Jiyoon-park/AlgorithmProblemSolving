def DFS(L, total):
    global maxx
    if L == N+1:
        if maxx < total:
            maxx = total
    else:
        if L + work[L][0] <= N+1:
            DFS(L+work[L][0], total+work[L][1])
        DFS(L+1, total)

N = int(input())
work = [[0,0]]
maxx = -(2**52)
for _ in range(N):
    days, pay = map(int, input().split())
    work.append([days, pay])
DFS(1, 0)
print(maxx)