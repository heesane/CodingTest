import sys

T = int(sys.stdin.readline().rstrip())
num_list = []
for _ in range(T):
    num_list.append(map(int,sys.stdin.readline().rstrip().split(' ')))
for i in range(T):
    print(sum(num_list[i]))