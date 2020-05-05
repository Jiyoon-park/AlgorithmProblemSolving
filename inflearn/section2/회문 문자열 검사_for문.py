N = int(input())

for tc in range(1, N+1):
    word = input()
    word = word.upper()
    size = len(word)
    for j in range(size//2):
        if word[j] != word[-1-j]:
            print('#{} NO'.format(tc))
            break
    else:
        print('#{} YES'.format(tc))