word1 = list(input())
word2 = list(input())
dict1 = {}
for w in word1:
    if w not in dict1:
        dict1[w] = 1
    else:
        dict1[w] += 1

dict2 = {}
for d in word2:
    if d not in dict2:
        dict2[d] = 1
    else:
        dict2[d] += 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')

