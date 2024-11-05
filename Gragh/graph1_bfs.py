from collections import deque


# BFS로 특정 위치를 방문하고 연결된 모든 노드들도 방문
def bfs(x, y):
    # 큐 생성 및 시작 노드 삽입
    queue = deque()
    queue.append((x, y))
    # 시작 노드 방문 처리
    graph[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 방향 정의
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위를 벗어나지 않고, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 방문 처리하고 큐에 추가
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return True


# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대해 BFS 수행
count = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if graph[i][j] == 0 and bfs(i, j):
            count += 1

print(count)
