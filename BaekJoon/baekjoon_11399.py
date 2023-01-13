N = int(input())
waiting = list(map(int,input().split(' ')))
waiting.sort()
result = 0
for i in range(1,N+1):
    result += sum(waiting[0:i])
print(result)