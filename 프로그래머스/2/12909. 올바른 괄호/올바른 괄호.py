def solution(string):
    str_stack = []

    if string[0] == ')':
        return False
    else:
        str_stack.append(string[0])

    for i in string[1:]:
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