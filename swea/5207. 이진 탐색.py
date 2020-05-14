T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    result = 0
    for num in B:
        lcnt = rcnt = 0
        l = 0
        r = N - 1
        i = 0
        direction = 'x'
        while l <= r:
            m = (l + r) // 2
            if A[m] == num:
                result += 1
                break
            elif A[m] < num:
                if direction[i] != 'r':
                    direction += 'r'
                    i += 1
                    l = m + 1
                    continue
                else:
                    break
            elif A[m] > num:
                if direction[i] != 'l':
                    direction += 'l'
                    i += 1
                    r = m - 1
                    continue
                else:
                    break

    print('#{} {}'.format(tc, result))


