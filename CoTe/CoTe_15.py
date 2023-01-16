N = int(input())
ant = list(map(int,input().split(' ')))
take = [0] * 100
take[0] = ant[0]
take[1] = max(ant[0],ant[1])
for i in range(2,N):
    take[i] = max(take[i-1],take[i-2]+ant[i])
print(take[N-1])