N = list(map(int,input()))
N.sort(reverse = True)
for i in range(len(N)):
    print(N[i],end='')