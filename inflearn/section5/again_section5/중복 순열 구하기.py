def DFS(n):
    global cnt
    if n == M:
        cnt += 1
        for j in range(M):
            print(p[j], end=" ")
        print()
    else:
        for i in range(1, N+1):
            p[n] = i
            DFS(n+1)


N, M = map(int, input().split())
p = [0]*N
cnt = 0
DFS(0)
print(cnt)