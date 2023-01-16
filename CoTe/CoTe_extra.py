# 정수 N, M을 입력 받기
N, M = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(N):
    array.append(int(input()))
coin_dict = dict()
## dict 초기화
for i in range(1,N+1):
    coin_dict[i] = 0
for i in range(1,N):
    for j in range(array[i],M+1):
        if i % array[j] == 0:
            coin_dict[i] += 1
if coin_dict[M] == 0:
    print(-1)
else:
    print(coin_dict[M])
        