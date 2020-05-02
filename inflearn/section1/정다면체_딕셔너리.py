N, M = map(int, input().split())
nums1 = list(range(1, N+1))
nums2 = list(range(1, M+1))

result = {}
for i in range(N):
    for j in range(M):
        temp = str(nums1[i] + nums2[j])
        if temp not in result:
            result[temp] = 1
        else:
            result[temp] += 1
maxV = 0
for val in result.values():
    if val > maxV:
        maxV = val

ans = []
for key, val in result.items():
    if val == maxV:
        ans.append(int(key))
ans.sort()

final = ''
for a in ans:
    final += str(a) + ' '
print(final)