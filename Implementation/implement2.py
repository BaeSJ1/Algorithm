'''
    <문제> 시각
    정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성
    # '완전탐색' 문제 유형
    # 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
    # 하루 = 24H = 1440M =  86400S -> 즉, 모든 경우는 86,400가지

'''
N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)