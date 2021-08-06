def check(stack):
    print(stack)
    if stack[0] == "X": return True
    if stack[0] == "O" and stack[1] == "O": return True
    if stack[0] == "O" and stack[1] == "X": return True
    return False

def out_of_range(_case, case):
    if _case[0] < len(case) and _case[1] < len(case) and _case[0] >= 0 and _case[1] >= 0:
        return False
    return True

def dfs(is_traced, stack, case, i, j):
    if len(stack) == 2:
        return check(stack)

    _cases = [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]
    for _case in _cases:
        if not out_of_range(_case, case) and not is_traced[_case[0]][_case[1]]:
            is_traced[_case[0]][_case[1]] = True
            stack.append(case[_case[0]][_case[1]])
            if not dfs(is_traced, stack, case, _case[0], _case[1]):
                return False
            stack.pop()
    return True

def trace(case):
    stack = []
    is_traced = [[False] * len(case[0]) for _ in range(len(case))]
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] == "P":
                is_traced[i][j] = True
                result = dfs(is_traced, stack, case, i, j)
                if not result: return False
                stack = []
                is_traced = [[False] * len(case[0]) for _ in range(len(case))]
    return True

def solution(places):
    answers = []
    
    for case in places:
        if trace(case): answers.append(1)
        else: answers.append(0)
    return answers

if __name__ == "__main__":
  places = [["OOOOP", "OOPOO", "POOOO", "OOOOO", "OOOOP"]]
  print(solution(places))
