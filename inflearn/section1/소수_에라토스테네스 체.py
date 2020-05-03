N = int(input())
count = [0]*(N+1)
result = 0
for i in range(2, N+1):
    if count[i] == 0:
        result += 1
        for j in range(i, N+1, i):
            count[j] = 1
print(result)