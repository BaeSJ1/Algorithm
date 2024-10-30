'''
    <문제> 왕실의 나이트
    8*8 좌표 평면, 나이트 이동(단, 나이트는 L자 로만 이동 가능)
        1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
        2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
    입력 받은 위치에서 이동가능한 경로의 수는?

    # 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
    # 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의
'''
# 현재 나이트 위치 입력 받기
n = input()  # a1
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1
print(result)
