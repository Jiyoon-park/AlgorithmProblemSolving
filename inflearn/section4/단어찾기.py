from _collections import deque
N = int(input())
word = deque()
used = []
for _ in range(N):
    word.append(input())
for _ in range(N-1):
    used.append(input())
while word:
    w = word.popleft()
    if w in used:
        continue
    else:
        print(w)