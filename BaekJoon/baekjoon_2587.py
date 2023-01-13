num_list =[]
for i in range(5):
    num_list.append(int(input()))
mean = sum(num_list) // 5
num_list.sort()
print(mean)
print(num_list[2])