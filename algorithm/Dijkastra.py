# 간선의 가중치가 동일한 경우 => bfs 사용
# 간선의 가중치가 있는 경우 => mst로 풀어야

# 하나의 시작 정점에서 끝 정점까지의 최단경로 => one to all
    # 다익스트라(dijkstra)알고리즘 => 음의 가중치 허용 X
    # 벨만-포드(bellman-ford) 알고리즘 => 음의 가중치 허용

# 모든 정점들에 대한 최단 경로 => all pair => 다익스트라 배워서 활용하면 된다.
    # 폴로이드-워샬(Floyd-Warshall) 알고리즘

# dijkstra 알고리즘 => mst 프림 알고리즘과 유사

V,E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    s,e,c = map(int, input().split())
    adj[s].append([e,c])

# dist, selected 배열 준비
INF = float('inf')
dist = [INF]*V
selected = [False]*V

# 시작점 선택
dist[0]=0

# 모든 정점이 선택될때까지
cnt = 0
while cnt <V:
    # 아직 선택되지 않고 dist값이 최소인 정점 : u
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min=dist[i]
            u = i
    # 정점 u의 최단 거리 결정
    selected[u] = True
    cnt += 1
    # 정점 u에 인접한 정점에 대해서 간선완화
    for w, cost in adj[u] : # 도착정점, 가중치
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)

