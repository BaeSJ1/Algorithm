'''
    <문제> 모험가 길드
    한 마을에 모험가 N명, N명의 모험가를 상대로 공포도 측정.
    공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행 가능.
    N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값은?
'''
N = int(input())
horror_levels = list(map(int, input().split()))
horror_levels.sort()

group = 0  # 총 그룹의 수
count = 1  # 현재 그룹에 포함된 모험가의 수 (먼저 1명은 포함되어야 함)
for x in horror_levels:
    if count >= x:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group += 1
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화
    else:
        count += 1
print(group)
