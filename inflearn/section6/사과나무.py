N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]
total = 0
mid = s = e = N//2
for i in range(N):
    for j in range(N):
        if abs(i-s) + abs(j-e) <= mid:
            total += trees[i][j]
print(total)
