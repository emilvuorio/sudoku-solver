

global board
board = [[1,0,7,6,8,3,0,4,0],
[0,4,2,9,1,0,0,0,6],
[0,6,8,0,0,7,0,3,0],
[0,0,0,1,3,2,7,9,0],
[0,0,0,0,0,8,0,2,1],
[2,0,9,7,6,0,3,8,0],
[4,7,3,0,0,0,0,0,8],
[8,0,0,0,0,0,0,6,0],
[9,0,0,0,7,0,0,0,3]]



def check_possible(y, x, n):
    global board
    for i in range(0,9):
        if board[y][i] == n:
            return False
    for i in range(0,9):
        if board[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if check_possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
            
    draw_sudoku()
    
        




def draw_sudoku():
    global board
    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

solve()

