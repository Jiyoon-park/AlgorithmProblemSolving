N = int(input())
apples = [list(map(int, input().split())) for _ in range(N)]
midi = N//2
midj = N//2
summ = 0
for i in range(N):
    for j in range(N):
        if abs(midi-i) + abs(midj-j) in range(N//2+1):
            summ += apples[i][j]
print(summ)