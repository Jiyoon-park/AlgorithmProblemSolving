N = int(input())
players = []
for _ in range(N):
    height, weight = map(int, input().split())
    players.append((height, weight))

players = sorted(players, key=lambda x:x[0], reverse=True)
canplay = 1
for i in range(1, N):
    for j in range(i):
        if players[i][1] < players[j][1]:
            break
    else:
        canplay += 1

print(canplay)