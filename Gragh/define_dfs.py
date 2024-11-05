def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],  # 노드 0번: 그래프에서 사용되지 않거나, 1부터 시작하기 떄문에 고려하지 않는다.
    [2, 3, 8],  # 노드 1번: 노드 1은 노드 2,3,8과 연결
    [1, 7],  # 노드 2번: 노드 2는 노드 1,7과 연결
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
