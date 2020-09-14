# 오아왼위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(si, sj):
    global cnt
    if mountain[si][sj] == end:
        cnt += 1
    else:
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and mountain[ni][nj] > mountain[si][sj]:
                visited[ni][nj] = 1
                DFS(ni, nj)
                visited[ni][nj] = 0

N = int(input())
mountain = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
minn = 2**52
maxx = -(2**52)
for x in range(N):
    for y in range(N):
        if mountain[x][y] < minn:
            minn = mountain[x][y]
        if mountain[x][y] > maxx:
            maxx = mountain[x][y]
start = minn
end = maxx
for i in range(N):
    for j in range(N):
        if mountain[i][j] == start:
            DFS(i, j)
print(cnt)