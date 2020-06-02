# 최소 힙에서 약간의 변형 => 음수로 수를 바꿔줄 것. 그리고 출력시엔 다시 -1 곱해주기.
import heapq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print((heapq.heappop(a))*-1)
    else:
        heapq.heappush(a, n*-1)