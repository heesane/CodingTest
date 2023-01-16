import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
num_list = []
for i in range(1,N+1):
    for j in range(1,N+1):
        num_list.append(i*j)
num_list.sort()
print(num_list[K])