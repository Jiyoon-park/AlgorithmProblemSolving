def DFS(L):
    global minn
    if L == N:
        cha = max(hav) - min(hav)
        if minn > cha:
            if len(set(hav)) ==3:
                minn = cha

    else:
        for i in range(3):
            hav[i] += money[L]
            DFS(L+1)
            hav[i] -= money[L]


N = int(input())

money = []
hav = [0]*3
minn = 2**53 -1
for _ in range(N):
    temp = int(input())
    money.append(temp)

DFS(0)
print(minn)