pann = [input().split() for _ in range(7)]

count = 0
for i in range(7):
    for j in range(3):
        temp = ''
        for k in range(j, j+5):
            temp += pann[i][k]
        if temp == temp[::-1]:
            count += 1

for j in range(7):
    for i in range(3):
        temp = ''
        for k in range(i, i+5):
            temp += pann[k][j]
        if temp == temp[::-1]:
            count += 1
print(count)