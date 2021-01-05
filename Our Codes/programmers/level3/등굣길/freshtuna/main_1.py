def solution(m, n, puddles):
    min_distance = [[1000000007] + [0 for _ in range(m)] for _ in range(n)]
    min_distance = [[1000000007 for _ in range(m + 1)]] + min_distance
    min_distance[1][1], min_distance[n][m] = -1000000008, -1
    for puddle in puddles:
        min_distance[puddle[0]][puddle[1]] = 100
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_distance[i][j] += min(min_distance[i - 1][j], min_distance[i][j - 1]) + 1
    return min_distance[n][m] % 1000000007
