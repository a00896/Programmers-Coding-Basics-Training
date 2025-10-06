# 두 수의 연산값 비교하기
def solution(a, b):
    ab = int(str(a) + str(b))
    answer = max(ab, 2 * a * b)
    return answer