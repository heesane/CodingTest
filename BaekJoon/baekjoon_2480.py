dice = list(map(int,input().split(' ')))
if dice[0] == dice[1] == dice[2]:
    print(10000+1000*dice[0])
elif dice[0] == dice[1] and dice[0]!= dice[2]:
    print(1000+100*dice[0])
elif dice[0] == dice[2] and dice[0]!= dice[1]:
    print(1000+100*dice[0])
elif dice[2] == dice[1] and dice[2]!= dice[0]:
    print(1000+100*dice[1])
else:
    print(max(dice)*100)