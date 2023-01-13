A,B = map(int,input().split(' '))
C = int(input())
B = B + C
if B >= 60:
    A = A + B // 60
    B = B % 60
    
    if A >= 24:
        A = A - 24 
print(A,end=' ')
print(B)

