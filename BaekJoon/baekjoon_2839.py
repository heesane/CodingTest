import time
num = int(input())
start_time = time.time()
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break
    num -= 3
    count += 1
else:
    print(-1)
  
end_time = time.time()
print('Elapsed time : %s' % (end_time - start_time))