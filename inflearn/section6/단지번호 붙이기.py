# 오아왼위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(si, sj):
    global res
    st = []
    st.append([si,sj])
    visited[si][sj] = 1
    num = 1
    while st:
        x, y = st.pop()
        for k in range(4):
            ni = x + dx[k]
            nj = y + dy[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and danji[ni][nj] == '1':
                visited[ni][nj] = 1
                danji[ni][nj] = '0'
                num += 1
                st.append([ni,nj])
    res.append(num)


N = int(input())
danji = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
res = []
for i in range(N):
    for j in range(N):
        if danji[i][j] == '1' and visited[i][j] == 0:
            DFS(i,j)
res.sort()
print(len(res))
for r in res:
    print(r)
