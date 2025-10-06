# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    for query in queries:
        k = query[2]
        tmp = []
        for i in range(query[0], query[1]+1):
            if(k < arr[i]):
                tmp.append(arr[i])

        if(tmp):
            answer.append(min(tmp))
        else:
            answer.append(-1)

    return answer

print(solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]]))