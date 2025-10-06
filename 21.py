# 코드 처리하기
def solution(code):
    mode = 0
    ret = ''

    for idx in range(len(code)):
        if(code[idx] == '1'):
            mode = (mode + 1) % 2
        else:
            if(idx % 2 == mode):
                ret = ret + code[idx]
            print(mode)
            
    if(ret == ''):
        ret = "EMPTY"
        
    answer = ret
    return answer