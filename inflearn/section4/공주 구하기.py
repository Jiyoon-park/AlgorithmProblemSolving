from _collections import deque

N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)

cnt = 1
while q:
    if len(q) == 1:
        break
    else:
       if cnt != K:
           t = q.popleft()
           q.append(t)
           cnt += 1
       else:
           q.popleft()
           cnt = 1
           continue
print(q[0])