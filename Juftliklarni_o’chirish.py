def remove(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack) if stack else "Empty String"

s = input().strip()
print(remove(s))