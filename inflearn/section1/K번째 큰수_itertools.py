import itertools

N, K = map(int, input().split())
nums = list(map(int, input().split()))

combinations = itertools.combinations(nums, 3)
result = []
for combi in combinations:
    if sum(combi) not in result:
        result.append(sum(combi))

result.sort()
print(result[-K])