from _collections import deque

N, M = map(int, input().split())
temp = list(map(int, input().split()))
dangers = deque()
for i in range(N):
    dangers.append((temp[i], i))

cnt = 1
ans = 0
turn = []
while dangers:
    t = dangers.popleft()
    maxV = max(dangers, key=lambda x:x[0])
    if t[0] < maxV[0]:
        dangers.append(t)
        cnt += 1
    else:
        turn.append(t)
        if t[1] == M:
            break

print(len(turn))

