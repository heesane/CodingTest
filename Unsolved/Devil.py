N,M = map(int,input().split(' '))
subject_list = list(map(int,input().split(' ')))
score_list = list(map(int,input().split(' ')))
hour = 24 * N
cnt = 0
time_list = []
while len(score_list) > 0:
    high_score = max(score_list)
    index = score_list.index(high_score)
    score = subject_list[index]
    reward = 100 - score
    
    running_time  = reward // high_score
    
    hour = hour - running_time
    print(running_time)
    cnt += score + running_time * high_score
        
    del subject_list[index]
    del score_list[index]
print(cnt)