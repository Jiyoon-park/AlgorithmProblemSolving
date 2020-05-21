N, M = map(int, input().split())
weights = list(map(int,input().split()))
weights.sort()

start = 0
end = N-1
count = 0
visited = [0]*N
while start <= end:
    if weights[start] + weights[end] <= M:
        count += 1
        visited[start] = visited[end] = 1
        start += 1
        end -= 1
    else:
        count += 1
        visited[end] = 1
        end -= 1
print(count)