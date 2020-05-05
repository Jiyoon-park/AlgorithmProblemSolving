N = int(input())

for tc in range(1, N+1):
    word = input().lower()
    if word == word[::-1]:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))
