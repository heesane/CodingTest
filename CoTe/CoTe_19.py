# Dijkstra Algorithm
# N = 도시 수 M = 통로 수 C = 정보를 보내는 도시
import heapq
N,M,C = map(int,input().split())
INF = int(1e9)
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
start = C
## 통로에 대한 정보
for _ in range(M):
    X,Y,Z = map(int,input().split())
    graph[X].append((Y,Z))
# 거리 찾기
def dijkstra(start):
    q = []
    # start 기준으로 시작, 거리는 0으로 초기화
    distance[start] = 0
    # 거리, 노드번호
    heapq.heappush(q,(0,start))
    while q:
        # dist = 거리, now = 노드번호
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance(i[0]):
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
print(dijkstra(start))
count = 0

for i in distance:
    if i != INF:
        count += 1

                       
