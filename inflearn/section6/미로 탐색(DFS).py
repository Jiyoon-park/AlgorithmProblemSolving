# 오아왼위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def DFS(i, j):
    global cnt
    if [i, j] == [6,6]:
        cnt += 1
        return
    else:
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < 7 and 0 <= nj < 7 and visited[ni][nj] == 0 and maze[ni][nj] == 0:
                visited[ni][nj] = 1
                DFS(ni, nj)
                visited[ni][nj] = 0

maze = [list(map(int, input().split())) for _ in range(7)]
visited = [[0]*7 for _ in range(7)]
cnt = 0
visited[0][0] = 1
DFS(0,0)
print(cnt)