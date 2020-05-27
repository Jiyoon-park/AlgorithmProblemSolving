sticks = input()

st = []
result = 0
for i in range(len(sticks)):
    if sticks[i] == '(':
        st.append(sticks[i])
    else:
        if sticks[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1
print(result)