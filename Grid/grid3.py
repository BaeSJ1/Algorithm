'''
    <문제> 곱하기 혹은 더하기
    각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
    숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성.
    (단, +보다 x를 먼저 계산하는 일방적인 방식과 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정)
'''
s = input()
data = list(s)
total = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if total <= 1 or num <= 1:
        total += num
    else:
        total *= num
print(total)
