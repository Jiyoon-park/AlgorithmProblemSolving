dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]

N = int(input())

heights = [list(map(int, input().split())) for _ in range(N)]
heights.insert(0, [0]*N)
heights.append([0]*N)
for height in heights:
    height.insert(0, 0)
    height.append(0)

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(heights[i][j] > heights[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
