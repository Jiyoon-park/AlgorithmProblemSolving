# prim => 정점 선택
import heapq

V, E = map(int, input().split())
adj = {i:[] for i in range(V+1)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])

# key, mst, 우선순위큐 준비
INF = float('inf')
key = [INF]*(V+1)
mst = [False]*(V+1)
pq = []
# 시작 정점 선택 : 0
key[0] = 0
# 큐에 시작 정점을 넣음 => (key, 정점인덱스)
# 우선순위큐 => 이진힙 => heapq 라이브러리 사용
heapq.heappush(pq,(0,0)) # 우선순위큐 => 원소의 첫번째 요소 => key를 우선순위로
result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    if mst[node] : continue     # 만약 필요없는(이미 mst면 스킵할게)
    # mst로 선택
    mst[node] = True
    result += k
    # key값 갱신 => key배열/q
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq, (key[dest], dest))
print(result)