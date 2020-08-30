from collections import deque
N = int(input())
q = deque()
for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'front':
        print(q[0] if len(q) else -1)
    elif order[0] == 'back':
        print(q[-1] if len(q) else -1)
    elif order[0] == 'pop':
        print(q.popleft() if len(q) else -1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(0 if len(q) else 1)
