N = int(input())
ox_list = []
for _ in range(N):
    ox_list.append(input())
for i in range(N):
    score = 0
    cnt = 0 
    for j in range(len(ox_list[i])):
        if ox_list[i][j]=='O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)