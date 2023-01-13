N,M = map(int,input().split(' '))
map_list = []

def find(x,y):
    # 예외처리에 관한 if
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    # 방문에 관한 if
    if map_list[x][y] == 0:
        map_list[x][y] = 1
        # x,y기준으로 상하좌우의 False / True 검사        
        find(x-1,y)
        find(x+1,y)
        find(x,y+1)
        find(x,y-1)            
        return True
    else:
        return False

for i in range(N):
    map_list.append(list(map(int,input())))
    
cnt = 0
for i in range(N):
    for j in range(M):
        if find(i,j) == True:
           cnt = cnt + 1
print(cnt)
            
