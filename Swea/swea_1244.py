'''
    교환 횟수만큼 교환을 해야 한다
    교환을 한 후에 얻은 숫자 중 가장 큰 값을 추출해야 한다.
    # DFS를 이용하여 모든 교환 가능한 경우를 탐색하고, 그 중 가장 큰 수를 찾아낸다.
    # 중복 체크를 위해 방문한 상태를 v 리스트에 저장하며, 이미 탐색한 상태를 반복하지 않도록 한다.(가지치기)
    # 교환 횟수가 제한되어 있고, 최대 교환 횟수는 10회로 작기 때문에 dfs로 모든 경우를 탐색해도 시간 내에 해결할 수 있다.
'''


def dfs(n):
    global result
    if n == N:  # 교환 횟수가 주어진 횟수에 도달했을 경우
        result = max(result, int("".join(map(str, lst))))  # 현재 상태에서 최대 값을 갱신
        return result  # 최종 결과 반환
    for i in range(L - 1):  # 교환 횟수는 갯수보다 -1 적게
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]  # 두 숫자의 위치를 교환

            chk = int("".join(map(str, lst))) * 10 + n  # 교환 후 숫자 계산
            if chk not in v:  # 중복된 값이면 방문하지 않음
                v.append(chk)  # 중복하지 않은 값은 방문 리스트에 추가
                result = dfs(n + 1)
            lst[i], lst[j] = lst[j], lst[i]
    return result  # 계산된 최종 결과 반환


T = int(input())
for test_case in range(1, T + 1):
    num, change = input().split()
    N = int(change)  # 교환 횟수
    L = len(num)  # 숫자판의 길이
    lst, v = [], []  # 숫자판의 숫자값을 저장하는 리스트, 중복방지를 위해 방문한 값을 저장하는 리스트
    for k in num:
        lst.append(int(k))  # 숫자 판의 숫자를 lst에 저장
    result = 0
    dfs(0)

    print(f'#{test_case} {result}')
