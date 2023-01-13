# Condition : N >= K
N,K = map(int,input().split())
count = 0
while N >= K:
    while N % K != 0:
        N = N - 1
        count = count + 1
    N = N // K
    count = count + 1
while N > 1:
    N = N - 1
    count = count + 1
print(count)