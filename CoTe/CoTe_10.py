N = int(input())
array = []
score = []
name = []
for i in range(N):
    info = input().split(' ')
    array.append((info[0],info[1]))
    score.append((info[1],i))
    name.append(info[0])

score.sort()
for i in range(N):
    print(name[score[i][1]],end=' ')








# first = input().split(' ')
# second = input().split(' ')
# prize = []
# if first[1]> second[1]:
#     prize.append(second[0])
#     prize.append()
#     print(second[0],' ',first[0])
# else:
#     print(first[0],' ',second[0])