N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
for _ in range(M):
    row, direction, count = map(int, input().split())
    newArray = [0]*N
    row -= 1
    #왼쪽으로
    if direction == 0:
        for i in range(N):
            if (i - count) < 0:
                position = N - abs(i-count)
            else:
                position = abs(i-count) % N
            newArray[position] = mat[row][i]
        mat[row] = newArray
    #오른쪽으로
    else:
        for i in range(N):
            position = abs(i+count) % N
            newArray[position] = mat[row][i]
        mat[row] = newArray

summ = 0
start = 0
end = N-1
for i in range(N):
    for j in range(start, end+1):
        summ += mat[i][j]
    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(summ)
