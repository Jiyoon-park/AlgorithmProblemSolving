def reverseSort(i, j, arr):
    start, end = i, j
    for k in range((end-start+1)//2):
        arr[start+k], arr[end-k] = arr[end-k], arr[start+k]
        # print(arr)

cards = list(range(21))
for _ in range(10):
    i, j = map(int, input().split())
    reverseSort(i, j, cards)

for card in cards[1:]:
    print(card, end=" ")
