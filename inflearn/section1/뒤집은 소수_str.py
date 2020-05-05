def reverse(x):
    x = x[::-1]
    i = 0
    while x[i] == '0':
        i += 1
    return int(x[i:])

def isPrime(x):
    global result
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    if count == 2:
        print(x, end=" ")

N = int(input())
nums = list(input().split())
result = []
for num in nums:
    target = reverse(num)
    isPrime(target)
