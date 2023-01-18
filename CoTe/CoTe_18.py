## Floyd-Warshall Algorithm
N,M = map(int,input().split(' '))
INF = int(1e9)
city = [[INF]*(1+N) for _ in range(1+N)]

## 초기화
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            city[i][j] = 0

## 출발,도착 = 1로 변경
for _ in range(M):
    start,end = map(int,input().split(' '))
    city[start][end] = 1
    city[end][start] = 1
    
## X : 최종 도착, K : 경유지
X,K = map(int,input().split(' '))
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            city[i][j] = min(city[i][j],city[i][k]+city[k][j]) 

## 1~K + K~X
total_dist = city[1][K]+city[K][X]
## 위의 경로중 하나라도 INF라면 -1
if total_dist >= INF:
    print(-1)
## 이외의 경우
else:
    print(total_dist)            
