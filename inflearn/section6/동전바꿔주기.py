def DFS(L, summ):
    global cnt
    if summ > T:
        return
    if L == k:
        if summ == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1,summ +(cv[L]*i))

T = int(input())
k = int(input())
cv = list()
cn = list()
for i in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt = 0
DFS(0, 0)
print(cnt)
