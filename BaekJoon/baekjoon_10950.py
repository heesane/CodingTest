N = int(input())
num_list = []
for i in range(N):
    num_list.append(map(int,input().split(' ')))
for i in range(N):
    print(sum(num_list[i]))