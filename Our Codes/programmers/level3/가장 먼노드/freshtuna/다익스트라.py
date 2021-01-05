from collections import Counter
import heapq

def solution(n, edge):
    # init
    distance = [20000 for _ in range(n + 1)]
    edges = [[] for _ in range(n + 1)]
    distance[1] = 0
    queue = [(value, index) for index, value in enumerate(distance)]
    heapq.heapify(queue)
    for data in edge:
        edges[data[0]].append(data[1])
        edges[data[1]].append(data[0])

    while queue:
        value, _from = heapq.heappop(queue)
        for _to in edges[_from]:
            if distance[_from] + 1 < distance[_to]:
                distance[_to] = distance[_from] + 1
                heapq.heappush(queue, (distance[_to], _to))

    return sorted(Counter(distance).items())[-2][1]
