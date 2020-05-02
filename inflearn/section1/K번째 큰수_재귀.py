def f(n, summ):
    global result
    if n == 3:
        if summ not in result:
            result.append(summ)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                f(n+1, summ+nums[i])
                used[i] = 0

N, K = map(int, input().split())
nums = list(map(int, input().split()))
p = [0]*3
used = [0]*N
result = []
f(0, 0)
result.sort()
print(result[-K])