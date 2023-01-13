from collections import deque


N,M = map(int,input().split(' '))
map_list = []

for i in range(N):
    map_list.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def find(pos_x,pos_y):
    Q = deque()
    Q.append((pos_x,pos_y))
    while Q:
        pos_x,pos_y = Q.popleft()
        for i in range(4):
            check_x = pos_x - dx[i]
            check_y = pos_y - dy[i]
            
            if check_x < 0 or check_x >= N or check_y < 0 or check_y >= M:
                continue
            
            if map_list[check_x][check_y] == 0:
                continue
            
            elif map_list[check_x][check_y] == 1:
                map_list[check_x][check_y] = map_list[pos_x][pos_y] + 1
                Q.append((check_x,check_y))
    return map_list[N-1][M-1]
print(find(0,0))