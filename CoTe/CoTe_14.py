X = int(input())
count = 0
num = [0]*101

for i in range(2,X+1):
    count = 0
    while True: 
        if i % 5 == 0:
            i = i // 5
            count += 1
        elif i % 3 == 0:
            i = i // 3
            count += 1
        elif i % 2 == 0:
            i = i // 2
            count += 1
        else:
            count+=1
            i= i - 1
        if i == 1:
            num[i] = count
            break
    if num[i-1] + 1 < num[i]:
        num[i] = num[i-1]+1
print(num[X])