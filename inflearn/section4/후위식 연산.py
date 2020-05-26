def calc(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2

form = input()
st = []
for f in form:
    if f.isdecimal():
        st.append(int(f))
    else:
        num2 = st.pop()
        num1 = st.pop()
        st.append(calc(num1, num2, f))
print(st[-1])