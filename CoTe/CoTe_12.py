N = int(input())
product_list = list(map(int,input().split(' ')))
M = int(input())
find_list = list(map(int,input().split(' ')))
answer = []
product_list.sort()
find_list.sort()
# for i in range(len(find_list)):
#     if find_list[i] not in product_list:
#         answer.append("no")
#     else:
#         answer.append("yes")        
end = len(product_list) - 1
start = 0
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
for find in find_list:
    if searching(find,0,len(product_list)) != None:
        answer.append("yes")
    else:
        answer.append("no")
for i in range(len(answer)):
    print(answer[i],end=" ")