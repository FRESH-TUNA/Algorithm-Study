from collections import deque

def solution(maps):
    return bfs(maps)

def bfs(maps):
    dy, dx = [1,-1,0,0], [0,0,1,-1]
    dist = [[ -1 for _ in range(len(maps[0]))] for _ in range(len(maps))] 
    dist[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        cy, cx = queue.popleft()
        for d in range(len(dy)):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if dist[ny][nx] == -1 and maps[ny][nx] == 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    queue.append((ny, nx))
    return dist[-1][-1]
