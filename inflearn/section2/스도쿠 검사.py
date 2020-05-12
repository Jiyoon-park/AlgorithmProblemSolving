def f(i, j):
    global result, sdoku
    si = i
    sj = j
    temp = set()
    temp.add(sdoku[si][sj])
    for k in range(8):
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        ni = si + dx[k]
        nj = sj + dy[k]
        temp.add(sdoku[ni][nj])
    if len(temp) != 9:
        result.append("NO")

sdoku = [list(map(int, input().split())) for _ in range(9)]
result = []
ans = 'YES'
for i in range(9):
    temp = set()
    for j in range(9):
        temp.add(sdoku[i][j])
    if len(temp) != 9:
        ans = 'NO'
        result.append('NO')
        break

for j in range(9):
    temp = set()
    for i in range(9):
        temp.add(sdoku[i][j])
    if len(temp) != 9:
        ans = 'NO'
        result.append('NO')
        break

middle = [1,4,7]
for i in middle:
    for j in middle:
        f(i, j)

if result:
    print("NO")
else:
    print("YES")