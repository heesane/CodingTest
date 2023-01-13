X = int(input())
N = int(input())
product_list = []
for i in range(N):
    product_list.append(list(map(int,input().split(' '))))
total = 0    
for i in range(N):
    total = total + product_list[i][0] * product_list[i][1]
if total == X:
    print("Yes")
else:
    print("No")