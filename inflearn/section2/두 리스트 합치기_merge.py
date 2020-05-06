N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

'''
c = a + b
c.sort()
for i in c:
    print(i, end=" ")
'''

c = []
p = q = 0
while p < N and q < M:
    if a[p] < b[q]:
        c.append(a[p])
        p += 1
    else:
        c.append(b[q])
        q += 1
if N < M :
    c = c + b[q:]
else:
    c = c + a[p:]

for i in c:
    print(i, end=" ")
