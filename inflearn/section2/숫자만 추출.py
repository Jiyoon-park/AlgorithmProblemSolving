word = input()
target = ''
for i in range(len(word)):
    if word[i].isdigit() == True:
        if word[i] == '0' and len(target) == 0:
            continue
        target += word[i]

target = int(target)
count = 0
for i in range(1, target+1):
    if target % i == 0:
        count += 1

print(target)
print(count)