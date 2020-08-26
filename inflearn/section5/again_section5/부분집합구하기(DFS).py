def DFS(v):
    if v == N+1:
        for i in range(1,N+1):
            if used[i]:
                print(i, end=" ")
        print()
    else:
        used[v] = 1
        DFS(v+1)
        used[v] = 0
        DFS(v+1)

N = int(input())
used = [0]*(N+1)
DFS(1)