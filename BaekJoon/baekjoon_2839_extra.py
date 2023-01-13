modify = input().split('-')
test = []
make = 0
for i in modify:
    make = 0
    temp = i.split('+')
    for j in temp:
        make += int(j)
    test.append(make)

first = test[0]
for i in range(1,len(test)):
    first -= test[i]
print(first)