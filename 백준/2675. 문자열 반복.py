T = int(input())
for tc in range(1,T+1):
    num, target = input().split()
    num = int(num)
    target = list(target)
    res = ''
    for tar in target:
        res += tar*num
    print(res)