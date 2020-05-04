N = int(input())

maxV = 0
for i in range(N):
    nums = list(map(int, input().split()))
    temp = len(set(nums))
    if temp == 1:
        ans = 10000 + nums[0]*1000
    elif temp == 3:
        ans = max(nums)*100
    else:
        start = nums[0]
        for j in range(1, temp):
            if start == nums[j]:
                ans = 1000+start*100
            else:
                ans = 1000+nums[1]*100
    # 가장 큰 값
    if maxV < ans:
        maxV = ans
print(maxV)