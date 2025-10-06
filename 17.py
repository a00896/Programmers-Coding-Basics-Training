# 공배수
def solution(number, n, m):
    answer = 1 if ((number % n == 0) & (number % m == 0)) else 0
    return answer