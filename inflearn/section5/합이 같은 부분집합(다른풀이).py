import sys
sys.stdin=open("input.txt", "r")

def dfs(n, k, summ):
    global ans, total
    if summ > total//2:
        return
    if n == k:
        if summ == (total-summ):
            print('YES')
            sys.exit(0)
    else:
        dfs(n+1, k, summ+nums[n])
        dfs(n+1, k, summ)

N = int(input())
nums = list(map(int, input().split()))
total = sum(nums)
used = [0]*N
dfs(0, N, 0)
print('NO')
