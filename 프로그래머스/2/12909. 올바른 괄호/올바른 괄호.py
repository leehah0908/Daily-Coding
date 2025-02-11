def solution(string):
    str_stack = []

    for i in string:
        if i == '(':
            str_stack.append(i)
        elif i == ')':
            if not str_stack:
                return False
            if str_stack[-1] == '(':
                str_stack.pop()

    if str_stack:
        return False
    return True