# Python program to convert infix to prefix

# Check if character is an operator
def isOperator(ch):
    return ch in ['+', '-', '*', '/', '^']

# Get precedence of operators
def operatorPrecedence(op):
    if op == '^':
        return 3
    if op in ['*', '/']:
        return 2
    if op in ['+', '-']:
        return 1
    return -1

# Convert infix expression to postfix notation
def convertInfixToPostfix(s):
    st = []
    res = ""
    sz = len(s)

    for i in range(sz):
        if s[i].isalnum():
            res += s[i]
        elif s[i] == '(':
            st.append(s[i])
        elif s[i] == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            while st and operatorPrecedence(s[i]) <= operatorPrecedence(st[-1]):
                res += st.pop()
            st.append(s[i])

    while st:
        res += st.pop()

    return res

# Convert infix expression to prefix notation
def convertToPrefix(infix):
    infix = infix[::-1]
    infix = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix])
    
    postfix = convertInfixToPostfix(infix)
    return postfix[::-1]

if __name__ == "__main__":
    s = "(a-b/c)*(a/k-l)"
    print(convertToPrefix(s))
