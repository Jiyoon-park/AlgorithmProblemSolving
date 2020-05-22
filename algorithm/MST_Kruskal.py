# kruskal => 간선 선택 => 가중치가 가장 낮은 간선부터 선택.
# 싸이클이 존재하면 다음으로 가장 낮은 간선 선택
# 싸이클 언제 생겨? => 대표자가 같을 때 연결하면 싸이클이 생긴다.
# 상호배타집합 연산 사용

def make_set(x):
    p[x] = x

def find_set(x):    # 내가 속한 집합의 대표자 찾기
    if p[x] == x : return x # 내가 대표자면 나를 반환
    else:
        # find_set(p[x])  # 내가 대표자가 아니면 부모 찾아 올라가기
        p[x] = find_set(p[x]) # path comprehension
        return p[x]

def union(x, y): # 랭크 확인
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
# 간선을 간선가중치를 기준으로 정렬
edges.sort(key=lambda x:x[2])

# make_set : 모든 정점에 대해서 집합을 생성
p = [0]*V
rank = [0]*V    # 내 노드의 서브트리의 깊이 => 더 깊은애를 부모
for i in range(V):
    make_set(i)

cnt = 0
result = 0
mst = []
# 모든 간선에 대해서 반복 => V-1개의 간선이 선택될때까지.
for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    # 싸이클이면 스킵 => =간선의 두 정점이 서로 같은 집합이면 스킵 => (find_set)
    if find_set(s) == find_set(e): continue
    # 싸이클이 아니면 간선을 선택
    # mst에 간선 정보 더하기 / 두 정점 합치기(union)
    result += c
    mst.append(edges[i])
    union(s,e)
    cnt += 1
    if cnt == V-1 : break

