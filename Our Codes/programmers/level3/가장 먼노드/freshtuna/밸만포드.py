from collections import Counter

def solution(n, edge):
    distance = [20000 for _ in range(n + 1)]
    distance[1] = 0

    for i in range(1, n + 1):
        for case in edge:
            x, y = case
            if distance[y] > distance[x] + 1:
                distance[y] = distance[x] + 1
            if distance[x] > distance[y] + 1:
                distance[x] = distance[y] + 1

    return sorted(Counter(distance).items())[-2][1]
