N = int(input())
schedules = []
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append((start,end))
schedules = sorted(schedules, key=lambda x:x[1])

count = 1
start = 0
for i in range(N):
    if schedules[start][1] <= schedules[i][0]:
        count += 1
        start = i
    else:
        continue
print(count)