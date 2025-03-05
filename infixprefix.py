# this function returns a Boolean Value
def is_operator(char):
    return char in {'+', '-', '*', '/', '^'}

# returns a number that represents a priority
# we are following a order of rule or operator precedence
# P - since in this code parenthesis is not included
# E - 3
# M - 2
# D - 2
# A - 1
# S - 1
def get_priority(operator):
    if operator in {'+', '-'}:
        return 1
    elif operator in {'*', '/'}:
        return 2
    elif operator in {'/', '^'}:
        return 3
    return 0

# a function that converts infix to prefix as stated in the variable name
def convert_infix_prefix(infix):
    infix = infix[::-1]
    # the purpose of this line of code is that it corrects the parenthesis
    # for example 3+4/(2 + 1) when reversed )1 + 2(/4+3, this also stores it in array
    infix = ['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix]

    # initialization of two stack variables
    operators = []
    operands = []

    # we will loop through the entire array
    for character in infix:
        # isalnum function checks if the character is alphanumerical
        # if operand we will append that character inside the operands stack
        if character.isalnum():
            operands.append(character)
        # If '(', push to operator stack
        elif character == '(':
            operators.append(character)
        # If ')', pop until '(' is found
        elif character == ')':
            while operators and  operators[-1] != '(':
                operands1 = operands.pop()
                operands2 = operands.pop()
                operator = operators.pop()
                operands.append(operator + operands1 + operands2)
            operators.pop() # remove the (
        # If operator, handle precedence
        else:
            while operators and get_priority(character) <= get_priority(operators[-1]):
                operands1 = operands.pop()
                operands2 = operands.pop()
                operator = operators.pop()
                operands.append(operator + operands1 + operands2)
            operators.append(character)

    while operators: # the remaining operators
        operands1 = operands.pop()
        operands2 = operands.pop()
        operator = operators.pop()
        operands.append(operator + operands1 + operands2)

    return operands[-1]

first_sample = "(1+2)/3*5-1"
second_sample = "1+2/(3*5-1)"
third_sample = "1+2/(3*5-1)"
print( convert_infix_prefix(first_sample))
print( convert_infix_prefix(second_sample))
print( convert_infix_prefix(third_sample))

sample_1 = "3+4/(2+1)"
print(convert_infix_prefix(sample_1))