N = int(input())

count = 0
for i in range(1, N+1):
    temp = 0
    for j in range(1, i+1):
        if i % j == 0:
            temp += 1
    if temp == 2:
        count += 1
print(count)