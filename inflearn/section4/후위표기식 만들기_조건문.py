result = ''
st = []
a = input()
for x in a:
    if x.isdecimal():
        result += x
    else:
        if x == '(':
            st.append(x)
        elif x == '*' or x == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                result += st.pop()
            st.append(x)
        elif x in '+-':
            while st and st[-1] != '(':
                result += st.pop()
            st.append(x)
        elif x == ')':
            while st and st[-1] != '(':
                result += st.pop()
            st.pop()
while st:
    result += st.pop()
print(result)
