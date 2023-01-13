def solution(s):
    answer = []
    
    str_dict = {}
    
    for index, str_some in enumerate(list(s)):
        if str_some in str_dict:
            answer.append(index - str_dict[str_some])
            str_dict[str_some] = index
        else:
            answer.append(-1)
            str_dict[str_some] = index            
            
    return answer
