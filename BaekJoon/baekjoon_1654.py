K,N = map(int,input().split())
lan_list = []
for _ in range(K):
    lan_list.append(int(input()))
start = 1
end = max(lan_list)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lan_list:
        total += i // mid
    if total < N:
        end = mid - 1
    elif total >= N:
        start = mid + 1
print(end)