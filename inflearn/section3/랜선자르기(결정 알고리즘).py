K, N = map(int, input().split())
have = []
for _ in range(K):
    have.append(int(input()))

maxlen = max(have)
l = 0
r = maxlen
maxV = 0
while True:
    mid = (l + r) // 2
    summ = 0
    for each in have:
        make = each // mid
        summ += make
    if summ >= N:
        if mid > maxV:
            maxV = mid
            l = mid+1
            continue
        else:
            break
    else:
        r = mid-1
        continue

print(maxV)