prio = {'(':3, ')':3, '+':2, '-':2, '*':1, '/':1}

result = []
st = []
form = input()
for f in form:
    if f.isdigit():
        result.append(f)
    else:
        if not st or f == '(':
            st.append(f)
        else:
            if f == ')':
                while st and st[-1] != '(':
                    result += st.pop()
                st.pop()
            while st and prio[st[-1]] <= prio[f]:
                result += st.pop()
            if f != ')':
                st.append(f)
while st:
    s = st.pop()
    result.append(s)

print(''.join(result))