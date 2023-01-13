def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())
bridge = []
cnt = []
for i in range(T):
    N,M = map(int,input().split(' '))
    bridge.append([N,M])

for i in range(T):
    n = bridge[i][0]
    m = bridge[i][1]
    
    cnt_test = factorial(m) // (factorial(n)*factorial(m-n))
    cnt.append(cnt_test)

for i in cnt:
    print(i)