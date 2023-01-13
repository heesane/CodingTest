N = int(input())
num = []
a = N // 10
b = N % 10
cnt = 0
while True:
    sum_num = a + b
    if sum_num >= 10:
        sum_num -= 10
    temp = b * 10 + sum_num
    cnt +=1
    if temp == N:
        break
    else:
        a = temp // 10
        b = temp % 10
print(cnt) 