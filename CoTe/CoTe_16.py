N = int(input())
glass_list = [0] * 100
glass_list[1] = 1
glass_list[2] = 3
for i in range(3,N+1):
    glass_list[i] = (glass_list[i-1] + 2*glass_list[i-2]) % 796796
print(glass_list[N])