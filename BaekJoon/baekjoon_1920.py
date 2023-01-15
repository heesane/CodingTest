import sys
def searching(find,start,end):
    while start <= end:
        middle = (start + end) // 2
        if product_list[middle] == find:
            return middle
        elif product_list[middle] > find:
            end = middle - 1
        elif product_list[middle] < find:
            start = middle + 1       
    return None
N = int(sys.stdin.readline().rstrip())
product_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())
find_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))
answer = []
product_list.sort()
end = len(product_list) - 1
start = 0
for find in find_list:
    if searching(find,start,end) != None:
        answer.append("1")
    else:
        answer.append("0")
for i in range(M):
    print(answer[i],end=" ")