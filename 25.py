# 이어 붙인 수
def solution(num_list):
    sum_odd = ''
    sum_even = ''
    for i in num_list:
        if(i % 2 != 0):
            sum_odd = sum_odd + str(i)
        else:
            sum_even = sum_even + str(i)
            
    answer = int(sum_odd) + int(sum_even)
    return answer