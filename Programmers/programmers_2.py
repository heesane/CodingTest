def solution(today, terms, privacies):
    answer = []
    check = []
    year,month,day = map(int,today.split('.'))
    now_total = year * 12 *28 + 28 * month + day
    for term in terms:
        types,dead_line = term.split()
        dead_line = int(dead_line)
        cnt = 0
        for privacie in privacies:
            # for문으로 가져오는 데이터 분리
            date,grade = privacie.split()
            past_year,past_month,past_day = map(int,date.split('.'))
            past_total = past_year * 12 *28 + 28 * past_month + past_day
            #Grade 와 types가 맞으면.
            if grade == types:
                past_total += 28*dead_line
                if now_total >= past_total:
                        answer.append(cnt+1)
            cnt+=1
    answer.sort()
    return answer