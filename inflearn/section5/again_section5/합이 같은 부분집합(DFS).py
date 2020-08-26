import sys
def DFS(L, summ):
    if summ > total//2:
        return
    if L == N:
        if summ == (total-summ):
            print('YES')
            sys.exit(0)
    else:
        DFS(L+1, summ+nums[L])
        DFS(L+1, summ)

N = int(input())
nums = list(map(int, input().split()))
total = sum(nums)
DFS(0, 0)
print('NO')

