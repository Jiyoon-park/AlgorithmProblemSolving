N = int(input())
nums = [0] + list(map(int, input().split()))
print(nums)
p = [0]*(N)

# nums를 순서대로 돌면서
# i의 위치는 p의 0의 개수가 nums[i]가 되는 그 다음 칸
i = 1
while i <= N:
    count = 0
    for j in range(len(p)):
        if p[j] == 0:
            count += 1
        if count == nums[i]+1:
            target = [j, i]
            break
    p[target[0]] = target[1]
    i += 1
for i in range(len(p)):
    print(p[i], end=' ')