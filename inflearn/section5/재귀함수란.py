def dfs(num):
    global result
    if num == 0:
        return
    else:
        dfs(num//2)
        print(num % 2, end='')

N = int(input())
result = []
dfs(N)
