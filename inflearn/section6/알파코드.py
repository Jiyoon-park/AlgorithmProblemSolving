temp = 'abcdefghijklmnopqrstuvwxyz'.upper()
alpha = {}
for idx, val in enumerate(temp):
    alpha[str(idx+1)] = val

def DFS(L):
    global cnt
    if L == len(n):
        ans = ''
        for r in res:
            # ans += chr(int(r)+64) 65부터 대문자 A
            ans += alpha[r]
        cnt += 1
        print(ans)
    else:
        if 0 < int(n[L]):
            res.append(n[L])
            DFS(L+1)
            res.pop()
            if L+1 < len(n) and int(n[L]+n[L+1]) <= 26:
                res.append(n[L]+n[L+1])
                DFS(L+2)
                res.pop()

n = list(input())
res = []
cnt = 0
DFS(0)
print(cnt)