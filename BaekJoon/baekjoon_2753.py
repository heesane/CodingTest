Year = int(input())

if Year % 4 == 0 and (Year % 100 != 0 or Year % 400 ==0 ):
    print(1)
else:
    print(0)