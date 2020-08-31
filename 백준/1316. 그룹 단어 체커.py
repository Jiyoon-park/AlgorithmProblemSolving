from collections import deque
N = int(input())

cnt = 0
for _ in range(N):
    temp = []
    word = deque(input())
    while word:
        w = word.popleft()
        if (w in temp) and (temp[-1] != w): break
        temp.append(w)
    else: cnt += 1
print(cnt)





