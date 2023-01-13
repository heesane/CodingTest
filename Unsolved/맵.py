#맵크기
N,M = map(int,input().split(' '))
#현재좌표 및 방향
pos_x,pos_y,direction = map(int,input().split(' '))

map_list = []
#맵그리기
for i in range(M):
    map_list.append(list(map(int,input().split(' '))))

move_x = [-1,0,1,0]
move_y = [0,-1,0,1]
cnt = 0
while(True):
    ## 북
    if direction == 0:
        pos_x = pos_x - move_x[direction]
        pos_y = pos_y - move_y[direction]
        if map_list[pos_x][pos_y] == 1:
            direction = 3
        else:
            map_list[pos_x][pos_y] = 2
            cnt = cnt + 1
    ## 동
    elif direction == 1:
        pos_x = pos_x - move_x[direction]
        pos_y = pos_y - move_y[direction]
        if map_list[pos_x][pos_y] == 1:
            direction = 0
        else:
            map_list[pos_x][pos_y] = 2
            cnt = cnt + 1    
    ## 남        
    elif direction == 2:
        pos_x = pos_x - move_x[direction]
        pos_y = pos_y - move_y[direction]
        if map_list[pos_x][pos_y] == 1:
            direction = 1
        else:
            map_list[pos_x][pos_y] = 2
            cnt = cnt + 1    
    ## 서        
    elif direction == 3:
        pos_x = pos_x - move_x[direction]
        pos_y = pos_y - move_y[direction]
        if map_list[pos_x][pos_y] == 1:
            direction = 2        
        else:
            map_list[pos_x][pos_y] = 2
            cnt = cnt + 1
    
    ## 사방이 바다        
    if map_list[pos_x-1][pos_y] == 1 and map_list[pos_x][pos_y-1] == 1 and \
       map_list[pos_x+1][pos_y] == 1 and map_list[pos_x][pos_y+1] == 1:
           break;
    
    ## 다 가본 곳
    if (map_list[pos_x-1][pos_y] == 2 or map_list[pos_x-1][pos_y] == 1) and (map_list[pos_x][pos_y-1] == 2 or map_list[pos_x][pos_y-1] == 1) and (map_list[pos_x+1][pos_y] == 2 or map_list[pos_x+1][pos_y] == 1) and (map_list[pos_x][pos_y+1] == 2 or map_list[pos_x][pos_y+1] == 1):
        
        if direction = 0:
            pos_y = pos_y - 1
        if direction = 1:
            pos_x = pos_x - 1
        if direction = 2:
            pos_y = pos_y - 1
        if direction = 3:
            pos_y = pos_y - 1
print(cnt)