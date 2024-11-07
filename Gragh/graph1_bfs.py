from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            count += 1

print(count)
