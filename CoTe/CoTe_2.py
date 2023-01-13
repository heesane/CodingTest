N,M,K = map(int,input().split(" "))
input_num = list(map(int,input().split(' ')))
input_num.sort()
max_first = input_num[N-1]
max_second = input_num[N-2]
total_num = 0
while True:
    for i in range(K):
        if M == 0:
            break
        total_num = total_num + max_first
        M = M - 1
    if M == 0:
        break
    total_num = total_num + max_second
    M = M - 1
print(total_num)

