def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n//a)
        n += (b-a) * (n//a)
    
    return answer * b