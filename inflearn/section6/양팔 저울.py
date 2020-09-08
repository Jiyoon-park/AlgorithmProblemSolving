def DFS(L, summ):
    global cann
    if L == N:
        if summ > 0:
            cann.add(summ)
    else:
        DFS(L+1, summ+nums[L])
        DFS(L+1, summ)
        DFS(L+1, summ-nums[L])


N = int(input())
nums = list(map(int, input().split()))
cann = set()
DFS(0, 0)
print(sum(nums)-len(cann))