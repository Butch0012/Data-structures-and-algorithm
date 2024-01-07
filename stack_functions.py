def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            # Check if the current closing bracket matches the last opening bracket
            if not stack or brackets[stack.pop()] != char:
                return False
             # If the stack is empty, the expression is balanced
    return not stack