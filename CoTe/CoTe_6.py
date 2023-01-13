knight = input()
find_col = ord(knight[0]) - 96
find_row = int(knight[1])

movings = [[-2,-1],[-2,1],[2,-1],[2,1],[1,2],[-1,2],[1,-2],[-1,-2]]
cnt = 0
for move in movings:
    col_num = find_col + move[0]
    row_num = find_row + move[1]

    if col_num >= 1 and col_num<=8 and row_num>=1 and row_num<=8:
        cnt = cnt + 1
    
print(cnt)