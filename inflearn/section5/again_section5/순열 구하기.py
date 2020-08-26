def DFS(n):
    global count
    if n == M :
        count += 1
        for j in range(M):
            print(p[j], end=" ")
        print()
    else:
        for i in range(1, N+1):
            if not used[i]:
                used[i] = 1
                p[n] = i
                DFS(n+1)
                used[i] = 0

N, M = map(int, input().split())
p = [0]*M
used = [0]*(N+1)
count = 0
DFS(0)
print(count)
