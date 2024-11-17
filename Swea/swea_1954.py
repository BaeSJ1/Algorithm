'''
    불규칙적인 경로로 배열을 채운다면 BFS나 DFS를 사용하지만, 이 문제는 규칙적인 방향 전환이기 때문에 간단한 반복문으로 해결
'''
t = int(input())

# 시계방향 이동: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1, t + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]  # n x n 배열 초기화

    x, y = 0, 0  # 시작 위치
    direction = 0  # 초기 방향: 오른쪽
    num = 1  # 시작 숫자

    while num <= n * n:
        snail[x][y] = num  # 현재 위치에 숫자 배치
        num += 1

        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]

        # 배열 범위를 벗어나거나 이미 채워진 경우 방향 변경
        # if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0: