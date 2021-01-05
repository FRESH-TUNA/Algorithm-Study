def solution(m, n, puddles):
    min_distance = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for puddle in puddles:
        min_distance[puddle[0]][puddle[1]] = -1
    min_distance[0][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if min_distance[i][j] == -1: min_distance[i][j] = 0
            else: min_distance[i][j] = min_distance[i - 1][j] + min_distance[i][j - 1]
    return min_distance[n][m] % 1000000007