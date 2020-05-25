nums, M = map(int, input().split())
nums = list(map(int, str(nums)))
st = []
cnt = 0
for num in nums:
    while st and M>0 and st[-1]<num:
        st.pop()
        M-=1
    st.append(num)
if M != 0:
    st = st[:-M]
for s in st:
    print(s, end="")

