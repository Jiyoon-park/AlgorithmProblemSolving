from collections import deque
N, K = map(int, input().split())
q = deque(x for x in range(1, N+1))
result = '<'
cnt = 0
while q:
    num = q.popleft()
    cnt += 1
    if cnt != K:
        q.append(num)
    else:
        result = result + str(num) + ', '
        cnt = 0
result = result[:-2] + '>'
print(result)

