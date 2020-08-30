from collections import deque
N = int(input())
card = deque(x for x in range(1, N+1))
while len(card) > 1:
    card.popleft()
    num = card.popleft()
    card.append(num)
print(card[0])