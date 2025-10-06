# 조건 문자열
def solution(ineq, eq, n, m):
    answer = 0
    if (eq == "="):
        if (ineq == "<"):
            if(n <= m):
                answer = 1
        else:
            if(n >= m):
                answer = 1
    else:
        if (ineq == "<"):
            if(n < m):
                answer = 1
        else:
            if(n > m):
                answer = 1
    return answer

ineq = "<"
eq = "="
n = 20
m = 50

print(solution(ineq, eq, n, m))
print(solution(">", "!", 41, 78))