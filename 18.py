# 홀짝에 따라 다른 값 반환하기
def solution(n):
    if((n % 2) == 0):
        sum = 0
        for i in range(0, n+1, 2):
            print(i)
            sum = sum + (i ** 2)
        answer = sum
    else:
        answer = ((n+1)/2)**2

    return answer