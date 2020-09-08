def DFS(n, time, score):
    global maxx
    if time > M:
        return
    if n == N:
        if score > maxx:
            maxx = score
    else:
        DFS(n+1, time+problems[n][1], score+problems[n][0])
        DFS(n+1, time, score)

N, M = map(int, input().split())
maxx = 0
problems = []
for _ in range(N):
    score, time = map(int, input().split())
    problems.append([score, time])

DFS(0, 0, 0)
print(maxx)