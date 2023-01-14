N = int(input())
member_list = []
for i in range(N):
    a,b = input().split(' ')
    a = int(a)
    member_list.append([a,b,i])
member_list.sort()
member_list.sort(key = lambda x : (x[0],x[2]))
for i in range(N):
    print(f"{member_list[i][0]} {member_list[i][1]}")