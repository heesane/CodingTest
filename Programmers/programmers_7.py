def solution(s):
    answer = ''
    take = len(s)
    if s % 2 ==0:
        a = s[take]+ s[take-1]
        answer = a
    else:
        a = s[take]
        answer = a
    return answer

print(solution("qweqdwqerqr"))