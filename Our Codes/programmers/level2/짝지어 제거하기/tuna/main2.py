def solution(s):
    s, stack = list(s), []

    for i in range(len(s)):
        if len(stack) == 0 or stack[-1] != s[i]: stack.append(s[i])
        else: stack.pop()

    if len(stack) == 0: return 1
    else: return 0
