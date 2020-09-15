from collections import deque

#오아왼위 + 대각선
dx = [0,1,1,1,0, -1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def BFS(i,j):
    q = deque()
    q.append([i,j])
    island[i][j] = 0
    while q:
        si, sj = q.popleft()
        for k in range(8):
            ni = si + dx[k]
            nj = sj + dy[k]
            if 0 <= ni < N and 0 <= nj < N and island[ni][nj] == 1:
                island[ni][nj] = 0
                q.append([ni,nj])

N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if island[i][j] == 1:
            cnt += 1
            BFS(i,j)
print(cnt)