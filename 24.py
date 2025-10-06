# 원소들의 곱과 합
def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a = a * i
        b = b + i
        
    answer = 0 if (a > b**2) else 1
    return answer