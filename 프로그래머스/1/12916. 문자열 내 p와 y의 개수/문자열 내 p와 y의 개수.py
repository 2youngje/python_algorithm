def solution(s):
    
    if s.count('p')+s.count('P') == s.count('y')+s.count('Y'):
        answer = True
    else :
        answer = False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(s)
    
    return answer