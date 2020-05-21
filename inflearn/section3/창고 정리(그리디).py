L = int(input())
heights = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    maxV = max(heights)
    minV = min(heights)
    maxIdx = heights.index(maxV)
    minIdx = heights.index(minV)
    heights[maxIdx] -= 1
    heights[minIdx] += 1

print(max(heights) - min(heights))