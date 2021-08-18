from collections import deque

def check(stack):
    if stack[0] == "O" and stack[1] == "O": return True
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
            if case[_case[0]][_case[1]] == "P":
                return False
            is_traced[_case[0]][_case[1]] = True
            stack.append(case[_case[0]][_case[1]])
            if not dfs(is_traced, stack, case, _case[0], _case[1]):
                return False
            stack.pop()
    return True


def bfs(is_traced, case, i, j):
    dy, dx = [1,-1,0,0], [0,0,1,-1]
    queue = deque([(i, j)])
    
    while queue:
        cy, cx = queue.popleft()
        for d in range(len(dy)):
            ny, nx = cy + dy[d], cx + dx[d]
            if not out_of_range([ny, nx], case) and not is_traced[ny][nx]:
                if case[ny][nx] == "P": return False
                is_traced[ny][nx] = True
                if abs(ny - i) + abs(nx - j) <= 1: queue.append((ny, nx))
    return True


def make_is_traced(case):
    return [[True if case[i][j] == "X" else False 
            for j in range(len(case[i]))] for i in range(len(case))]

def trace(case):
    stack = []
    is_traced = make_is_traced(case)
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] == "P":
                is_traced[i][j] = True
                result = dfs(is_traced, stack, case, i, j)
                if not result: return False
                stack = []
                is_traced = make_is_traced(case)
                
    return True

def bfs_trace(case):
    is_traced = make_is_traced(case)
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] == "P":
                is_traced[i][j] = True
                result = bfs(is_traced, case, i, j)
                if not result: return False
                is_traced = make_is_traced(case)
    return True

def solution(places):
    answers = []
    
    for case in places:
        if bfs_trace(case): answers.append(1)
        else: answers.append(0)
    return answers

if __name__ == "__main__":
  places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
  print(solution(places))
