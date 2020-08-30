def createNewNum(strN, num):
    global cnt
    cnt += 1
    return strN[-1] + num[-1]

N = int(input())
newN = 0
strN = str(N)
cnt = 0
while N != int(newN):
    num = 0
    for i in range(len(strN)):
        num += int(strN[i])
    newN = createNewNum(strN, str(num))
    strN = newN
print(cnt)