def solution(s):
    answer, stack, flag = 0, [], True
    for _ in range(len(s)):
        for i in s:
            if i in ["[", "{", "("]: stack.append(i)
            elif len(stack) > 0 and i == "]" and stack[-1] == "[": stack.pop()
            elif len(stack) > 0 and i == "}" and stack[-1] == "{": stack.pop()
            elif len(stack) > 0 and i == ")" and stack[-1] == "(": stack.pop()
            else: 
                flag = False 
                break
        if len(stack) == 0 and flag: answer += 1
        s, stack, flag = s[-1] + s[0:-1], [], True
    return answer

if __name__ == "__main__":
    print(solution("[](){}"))
