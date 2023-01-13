T = int(input())
num_list = []
for i in range(T):
    num_list.append(map(int,input().split(' ')))
for i in range(T):
    print(f"Case #{i+1}: {sum(num_list[i])}")