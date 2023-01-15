num = int(input())
mean_list = []
for _ in range(num):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/score[0])*100
    mean_list.append(per)
for i in range(len(mean_list)):
    print(f"{mean_list[i]:.3f}%")