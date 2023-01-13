## Input
N = int(input())
Movings = input().split()
## Starting Point
pos_x,pos_y = 1,1

## L R U D
drow = [0,0,-1,1]
dcol = [-1,1,0,0]
can_move = ['L','R','U','D']
for move in Movings:
    for i in range(len(can_move)):
        if move == can_move[i]:
            test_x = pos_x + drow[i]
            test_y = pos_y + dcol[i]
    if test_x < 1 or test_x > N or test_y < 1 or test_y > N:
        continue
    pos_x = test_x
    pos_y = test_y
print(pos_x,pos_y)