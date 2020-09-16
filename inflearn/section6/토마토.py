from collections import deque
import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(well):
    q = well
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and box[ni][nj] ==0:
                visited[ni][nj] = visited[si][sj] + 1
                q.append([ni,nj])

M, N = map(int, input().split()) # 가로, 세로
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

well = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            well.append([i,j])
            visited[i][j] = 1
        if box[i][j] == -1:
            visited[i][j] = -1
BFS(well)
maxx = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] > maxx:
            maxx = visited[i][j]
        if visited[i][j] == 0:
            print(-1)
            sys.exit()
print(maxx-1)