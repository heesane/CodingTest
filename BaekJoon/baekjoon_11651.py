N = int(input())
pos_list = []
for _ in range(N):
    x,y = map(int,input().split(' '))
    pos_list.append([y,x])
pos_list.sort()
for i in range(len(pos_list)):
    print(f"{pos_list[i][1]} {pos_list[i][0]}")