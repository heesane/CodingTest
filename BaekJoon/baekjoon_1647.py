def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
            
N, M = map(int,input().split())
house = [0] * (N+1)
roads = []
for i in range(N+1):
    house[i] = i
# a,b = 집 c = 유지비용
for _ in range(M):
    a,b,c = map(int,input().split())
    roads.append([c,a,b])

roads.sort()
total_cost = 0
max_cost = 0 
for road in roads:
    cost,a,b = road
    if find_parent(house,a) != find_parent(house,b):
        union_parent(house,a,b)
        total_cost += cost
        max_cost = cost
print(total_cost-max_cost)
