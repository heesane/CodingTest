N = int(input())
num_list = list(map(int, input().split()))

num_dict = dict()

for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
M = int(input())
find_list = list(map(int, input().split()))

for i in find_list:
    if i in num_dict:
        print(num_dict[i], end=' ')    
    else:
        print(0, end=' ')