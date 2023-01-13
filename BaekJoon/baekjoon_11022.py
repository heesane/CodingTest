import sys
T = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(T):
    num_list.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
for i in range(T):
    print(f"Case #{i+1}: {num_list[i][0]} + {num_list[i][1]} = {num_list[i][0]+num_list[i][1]}")