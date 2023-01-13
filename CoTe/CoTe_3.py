N,M = map(int,input().split(' '))
CardList = []
for i in range(N):
    CardList.append(list(map(int,input().split(' '))))
    CardList[i] = min(CardList[i])
print(max(CardList))
    