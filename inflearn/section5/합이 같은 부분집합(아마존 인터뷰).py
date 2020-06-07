def dfs(n, k, summ):
    global ans
    if n == k:
        temp = []
        for i in range(N):
            if used[i] == 1 :
                temp.append(nums[i])
        temp2 = []
        for num in nums:
            if num not in temp:
                temp2.append(num)
        if sum(temp) == sum(temp2):
            ans = 'YES'
            return ans
    else:
        used[n] = 1
        dfs(n+1, k, summ+nums[n])
        used[n] = 0
        dfs(n+1, k, summ)


N = int(input())
ans = 'NO'
nums = list(map(int, input().split()))
used = [0]*N
dfs(0, N, 0)
print(ans)
