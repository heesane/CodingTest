N,K = map(int,input().split(' '))
first = list(map(int,input().split(' ')))
second = list(map(int,input().split(' ')))
first.sort()
second.sort(reverse = True)
count = 0
for k in range(K):
    if first[k] < second[k]:
        first[k],second[k] = second[k],first[k]
    else:
        break


print(sum(first))