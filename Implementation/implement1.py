"""
    <문제> 상하좌우
    NxN 크기의 정사각형 공간 위
    가장 왼쪽 위 좌표: (1,1), 가장 오른쪽 아래 좌표: (N,N), 시작좌표: (1,1)
    (단, NxN 크기의 정사각형 공간을 벗어나느 움직임 무시)
"""
n = int(input())  # 5
plans = input().split()  # R R R U D D

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
