def check(mid):
    horse = 1
    start = 0
    for i in range(1, N):
        if magugan[start] + mid <= magugan[i]:
            horse += 1
            start = i
        else:
            continue
    return horse

N, C  = map(int, input().split())
magugan = []
for _ in range(N):
    magugan.append((int(input())))

magugan.sort()
l = min(magugan)
r = max(magugan)
maxV = 0
while l <= r:
    mid = (l + r) //2
    if check(mid) >= C:
        if maxV < mid:
            maxV = mid
        l = mid+1
        continue
    else:
        r = mid-1
        continue

print(maxV)
