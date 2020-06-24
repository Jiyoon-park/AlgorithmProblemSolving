import itertools
def dfs(n, k):
    global cnt
    if n == k:
        cnt += 1
        for j in range(M):
            print(p[j], end=' ')
        print()
    else:
        for i in range(N):
            if used[i] == 0:
                # used[i] = 1
                p[n] = nums[i]
                dfs(n+1, k)
                # used[i] = 0

N, M = map(int, input().split())
nums = list(range(1, N+1))
used = [0]*N
p = [0]*M
cnt = 0
dfs(0,M)
print(cnt)