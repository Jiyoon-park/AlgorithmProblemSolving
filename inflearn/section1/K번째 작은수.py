T = int(input())
for tc in range(1,T+1):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = nums[s-1:e]
    nums.sort()
    print('#{} {}'.format(tc, nums[k-1]))