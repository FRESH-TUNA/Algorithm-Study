from collections import deque

def changeable(cur_word, word):
    diff = [True for x, y in zip(cur_word, word) if x != y]
    if len(diff) == 1: return True
    else: return False

def solution(begin, target, words):
    visited = set([0])
    words = [begin] + words
    queue = deque([(0, 0)])
    while queue:
        index, count = queue.popleft()
        if words[index] == target: return count
        for y, word in enumerate(words):
            if changeable(words[index], word) and y not in visited:
                queue.append((y, count + 1))
                visited.add(y)
    return 0
