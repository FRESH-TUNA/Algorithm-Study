def solution(verifiers, nodes):
    stack = dict()
    answer = dfs(stack, verifiers, nodes)
    # for i in range(len(nodes)):
    #     stack.update({nodes[i]: 0})
    #     answer += dfs(stack, verifiers, nodes)
    #     stack.pop(nodes[i])
    return answer


def dfs(stack, verifiers, nodes):
    answer = 0
    if len(stack) == len(nodes):
        if verify(stack, verifiers):
            answer += 1
    else:
        for i in range(len(nodes)):
            if nodes[i] not in stack:
                stack.update({nodes[i]: len(stack)})
                answer += dfs(stack, verifiers, nodes)
                stack.pop(nodes[i])
    return answer


def verify(stack, verifiers):
    for i in range(len(verifiers)):
        case = verifiers[i]
        difference = abs(stack[case[0]] - stack[case[2]]) - 1
        operator, condition = case[-2], int(case[-1])

        if not _verify(difference, operator, condition):
            return False
    return True


def _verify(difference, operator, condition):
    if operator == '>' and difference > condition:
        return True
    elif operator == '<' and difference < condition:
        return True
    elif operator == '=' and difference == condition:
        return True
    else:
        return False


if __name__== "__main__" :
    n = 2
    # answer = 3648
    # verifiers = ["M~C<2", "C~M>1"], answer = 0
    verifiers = ["N~F=0", "R~T>2"]
    nodes = ["A", "C", "F", "J", "M", "N", "R", "T"]
    answer = solution(verifiers, nodes)
    print(answer)