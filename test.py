

#board = [[0,0,0,0,0,0,0,0,0],
 #           [0,0,0,0,0,0,0,0,0],
  #          [0,0,0,0,0,0,0,0,0],
   ##        [0,0,0,0,0,0,0,0,0],
     #       [0,0,0,0,0,0,0,0,0],
      #      [0,0,0,0,0,0,0,0,0],
       #     [0,0,0,0,0,0,0,0,0],
        #    [0,0,0,0,0,0,0,0,0]]

board = [[0,0,0,0,0,0,0,0,0],
[9,3,0,2,0,0,0,8,7],
[5,0,4,0,0,0,0,0,6],
[0,0,0,4,0,0,0,6,0],
[7,5,0,0,0,0,1,0,8],
[0,2,8,0,0,0,0,9,0],
[0,0,0,0,2,0,9,0,0],
[8,9,0,0,0,5,0,0,0],
[0,7,0,0,1,0,0,0,0]]

def generate(board):
    
    import random
    draw_sudoku()
  
    for i in range(20):
        random_row = random.randint(0,8)
        random_column = random.randint(0,8)
        if board[random_row][random_column] == 0:
            for n in range(10):
                random_number = random.randint(1,9) 
                if check_possible(random_row, random_column, random_number):
                    board[random_row][random_column] = random_number

    draw_sudoku(board)




def check_possible(board, y, x, n):
    
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

def solve(board):
    
    
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if check_possible(board, y,x,n):
                        board[y][x] = n
                        #draw_sudoku()
                        #time.sleep(0.1)
                        solve(board)
                        board[y][x] = 0
                return
    draw_sudoku(board)
    
    
    input()
    
        
def draw_sudoku(board):

    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

draw_sudoku(board)
#generate()
solve(board)

