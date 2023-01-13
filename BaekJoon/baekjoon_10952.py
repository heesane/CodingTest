num = []
while True:
    a,b = map(int,input().split(' '))
    if a == 0 and b == 0:
        break
    num.append([a,b])
for i in range(len(num)):
    print(sum(num[i]))