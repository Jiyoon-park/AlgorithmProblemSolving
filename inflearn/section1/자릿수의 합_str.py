def digit_sum(x, lenn):
    summ = 0
    for i in range(lenn):
        summ += int(x[i])
    return summ

N = int(input())
nums = list(input().split())

maxV = 0
for x in nums:
    if maxV < digit_sum(x, len(x)):
        maxV = digit_sum(x, len(x))
        ans = x
print(ans)