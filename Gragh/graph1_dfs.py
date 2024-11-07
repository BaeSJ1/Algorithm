def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    return False


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
