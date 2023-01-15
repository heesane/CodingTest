N,M = map(int,input().split())
wood_list = list(map(int,input().split(' ')))
start = 1
end = max(wood_list)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in wood_list:
        if i > mid:
            total += i - mid
    if total < M:
        end = mid - 1
    elif total >= M:
        start = mid + 1
print(end)