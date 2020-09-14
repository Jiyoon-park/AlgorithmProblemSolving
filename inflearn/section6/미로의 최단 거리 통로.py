from collections import deque

# 오아왼위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(start):
    q = deque()
    q.append(start)
    i, j = start
    visited[i][j] = 1
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            if [ni, nj] == [6, 6]:
                return visited[si][sj]
            if 0 <= ni < 7 and 0 <= nj < 7:
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append([ni,nj])
                    visited[ni][nj] = visited[si][sj] + 1
    return -1


maze = [list(map(int, input().split())) for _ in range(7)]
visited = [[0]*7 for _ in range(7)]
ans = BFS([0,0])
print(ans)