def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():