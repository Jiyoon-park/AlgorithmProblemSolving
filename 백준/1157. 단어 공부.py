from collections import Counter
word = input()
word = word.upper()

counter = Counter(word)
maxx = max(x for x in counter.values())
res = []
for key, val in counter.items():
    if val == maxx:
        res.append(key)

print('?' if len(res)>1 else res[-1])