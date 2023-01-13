N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
num_list.sort()
for i in range(N-1,-1,-1):
    print(num_list[i],end=" ")