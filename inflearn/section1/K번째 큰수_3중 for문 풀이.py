N, K = map(int, input().split())
nums = list(map(int, input().split()))
res = set()
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(nums[i] + nums[j] + nums[m])
res = list(res)
res.sort(reverse=True)
print(res[K-1])
