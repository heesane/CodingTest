# 부모 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
# 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int,input().split())
parent = [0] * (N+1)
answer = []

for i in range(N+1):
    parent[i] = i 

for i in range(M):
    opcode,a,b = map(int,input().split())
    # 0 : 합치기
    if opcode == 0:
        union_parent(parent,a,b)
    # 1 : 같은 팀 여부
    elif opcode == 1:
        # 맞는 경우
        if find_parent(parent,a) == find_parent(parent,b):
            answer.append('YES')
        # 틀린 경우
        else:
            answer.append('NO')

for i in range(len(answer)):
    print(answer[i])
    
print(parent)