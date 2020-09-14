from collections import deque

s, e = map(int, input().split())
maxx = 10000
dis = visited = [0]*(maxx+1)
visited[s] = 1
dis[s] = 0
q = deque()
q.append(s)
while q:
    now = q.popleft()
    if now == e:
        break
    for next in (now-1, now+1, now+5):
        if 0 < next <= maxx:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
                dis[next] = dis[now] + 1
print(dis[e])

