# import sys
from collections import deque
# 오아왼위
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# sys.setrecursionlimit(10**6) <= 재귀로 풀 경우 넣어주기

def DFS(x,y,k):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        si, sj = q.popleft()
        for z in range(4):
            ni = si + dx[z]
            nj = sj + dy[z]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and area[ni][nj] > k:
                visited[ni][nj] = 1
                q.append([ni,nj])

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
res = 0
for k in range(100):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > k:
                cnt += 1
                DFS(i,j,k)
    res = max(res,cnt)
    if cnt== 0:
        break
print(res)