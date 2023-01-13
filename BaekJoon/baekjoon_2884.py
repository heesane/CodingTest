H,M = map(int,input().split(' '))
if M - 45 < 0:
    M = 15 + M
    H = H - 1
elif M - 45 >= 0:
    M = M - 45
if H < 0:
    H = 24 + H
print(H,end=' ')
print(M)