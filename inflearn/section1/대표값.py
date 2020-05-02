N = int(input())
nums = list(map(int, input().split()))

avgScore = sum(nums)/N
avgScore = int(avgScore + 0.5)

# avgScore = round(sum(nums)/N) -> 오류 발생/ round_half_up이 아닌 round_half_even 방식이기 때문
# round_half_even은 정확한 절반일 때 짝수쪽으로 간다.
# a = 4.5 , b = 5.5
# round(a) // 4
# round(b) // 6

minV = 2147000000
for idx, val in enumerate(nums):
    target = abs(avgScore-val)
    if target < minV:
        minV = target
        ansIdx = idx
        ansVal = val
    # 답이 같을 경우
    elif target == minV:
        # 점수가 높은 친구 출력
        if ansVal < val:
            ansVal = val
            ansIdx = idx
        # 점수가 같다면 번호가 빠른 학생 출력
        elif ansIdx > idx:
            ansIdx = idx

print(avgScore, ansIdx+1)
