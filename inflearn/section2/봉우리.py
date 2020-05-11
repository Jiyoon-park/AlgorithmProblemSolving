def f(i, j):
    global count
    si = i
    sj = j
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        ni = si + dx[k]
        nj = sj + dy[k]
        if 0 <= ni < N and 0 <= nj < N:
            if heights[ni][nj] < heights[si][sj]:
                continue
            else:
                break
    else:
        count += 1

N = int(input())
for _ in range(N):
    heights = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            f(i,j)

    print(count)