# 더 크게 합치기
def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    answer = max(ab, ba)
    return answer