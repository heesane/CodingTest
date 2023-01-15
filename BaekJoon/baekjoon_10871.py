N,X = map(int,input().split(' '))
num_list = list(map(int,input().split(' ')))
num = list(filter(lambda x : x< X,num_list))
for i in range(len(num)):
    if i == len(num) - 1:
        print(f"{num[i]}")
        break
    print(f"{num[i]}",end=' ')