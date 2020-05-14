N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
l = 0
r = N-1
while l <= r:
    m = (l+r)//2
    if nums[m] == M:
        print(m+1)
        break
    elif nums[m] < M:
        l = m+1
    else:
        r = m-1
