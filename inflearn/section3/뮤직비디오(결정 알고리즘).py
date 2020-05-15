def Count(capacity):
    cnt = 1
    summ = 0
    for song in songs:
        if summ + song > capacity:
            cnt += 1
            summ = song
        else:
            summ += song
    return cnt

N, M = map(int, input().split())    # N = 곡 개수, M = dvd 개수
songs = list(map(int, input().split()))

maxx = max(songs)
l = 1
r = sum(songs)
minV = 1000000
while l <= r:
    mid = (l + r) // 2
    if mid >= maxx and Count(mid) <= M:
        if minV > mid:
            minV = mid
            r = mid - 1
            continue
    else:
        l = mid + 1
        continue

print(minV)