# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        if(included[i]):
            sum = sum + a + d * i
    answer = sum
    return answer

print(solution(3,4,[True,False,False,True,True]))