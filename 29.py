# 수열과 구간 쿼리 3
def solution(arr, queries):
    answer = arr
    tmp = 0
    for i in queries:
        # tmp = answer[i[0]] 
        # answer[i[0]] = answer[i[1]]
        # answer[i[1]] = tmp
        answer[i[0]], answer[i[1]] = answer[i[1]], answer[i[0]]
    return answer