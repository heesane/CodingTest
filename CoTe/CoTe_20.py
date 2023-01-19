# Dijkstra Algorithm
# N = 도시 수 M = 통로 수 C = 정보를 보내는 도시
import heapq
N,M,C = map(int,input().split())
INF = int(1e9)
# 시작을 기준으로 해당 노드까지 걸리는 길이
distance = [INF] * (N+1)
# 노드에 대한 정보
graph = [[] for _ in range(N+1)]
# 정보를 보내는 도시
start = C
## 통로에 대한 정보
for _ in range(M):
    X,Y,Z = map(int,input().split())
    graph[X].append((Y,Z))
# 거리 찾기
q = []
distance[start] = 0
heapq.heappush(q,(0,start))
# 우선순위 큐에 거리와 노드 번호 삽입
# 우선 순위 큐에 내용이 있으면,
while q:
    # dist = 시작부터 now까지의 거리, now = 노드번호
    dist,now = heapq.heappop(q)
        
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        # i[0] : 도시 정보, i[1] : 거리 
        cost = dist + i[1]
        # 시작+다른 노드+현재 노드까지의 거리 < 시
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
                       
count = 0
max_d = 0
for i in distance:
    if i != INF:
        count += 1
        max_d = max(i,max_d)
print(count - 1,max_d)
