'''
    알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
    모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
    예) K1KA5CB7  ->  ABCKK13
'''
data = input()
result = []
value = 0

# input 문자열로 받았으니까 바로 이렇게 가능
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

# 알파벳으로 오름차순 / 정렬 복잡도: O(nlogn)
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))
