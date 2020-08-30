from collections import Counter
N = int(input())
maxx = 0
for _ in range(N):
    nums = Counter(map(int, input().split()))
    maxV = max(x for x in nums.values())
    if maxV == 4:
        res = 50000 + 5000*[x for x in nums][0]
    elif maxV == 3:
        for key, val in nums.items():
            if val == 3:
                res = 10000 + key*1000
    elif maxV == 2:
        if len(nums) == 2:
            res = 2000 + sum([500*x for x in nums])
        else:
            for key, val in nums.items():
                if val == 2:
                    res = 1000 + key*100
    else:
        res = max([x for x in nums])*100

    if maxx < res:
        maxx =res
print(maxx)
