def digit_sum(x):
    summ = 0
    # 일의 자리 -> 십의 자리 -> ... -> 자릿수 하나씩 잘라내면서 더하기
    while x > 0 :
        summ += x % 10
        x = x//10
    return summ

N = int(input())
nums = list(map(int, input().split()))

maxV = 0    # -2147000000
for x in nums:
    if maxV < digit_sum(x):
        maxV = digit_sum(x)
        ans = x
print(ans)