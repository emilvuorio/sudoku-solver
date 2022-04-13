<<<<<<< HEAD
global amount
amount = 0
global board
#board = [[0,0,0,0,0,0,0,0,0],
 #           [0,0,0,0,0,0,0,0,0],
  #          [0,0,0,0,0,0,0,0,0],
   ##        [0,0,0,0,0,0,0,0,0],
     #       [0,0,0,0,0,0,0,0,0],
      #      [0,0,0,0,0,0,0,0,0],
       #     [0,0,0,0,0,0,0,0,0],
        #    [0,0,0,0,0,0,0,0,0]]

board = [[4,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,5,0],
[0,7,0,0,4,0,3,6,0],
[0,2,0,0,0,0,0,0,1],
[0,0,0,0,3,0,0,0,5],
[0,0,6,8,0,0,2,3,0],
[0,0,8,0,0,9,0,0,0],
[0,0,0,0,0,0,0,0,2],
[0,6,0,0,1,0,7,4,0]]

def generate():
    global board
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

    draw_sudoku()

=======
import time

global board
>>>>>>> eda0b8139d6701d811c8445cfa7ff26a263f7d33

board = [[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]]


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
    global amount
    global board
    import time
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if check_possible(y,x,n):
                        board[y][x] = n
                        #draw_sudoku()
                        #time.sleep(0.1)
                        solve()
                        board[y][x] = 0
                return
    draw_sudoku()
    
        


    draw_sudoku()
    print("Solved in " + "--- %s seconds ---" % (time.time() - start_time))
    
    
    input()
    
        
def draw_sudoku():
    global board
    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

start_time = time.time()
print(start_time)
draw_sudoku()
<<<<<<< HEAD
#generate()
=======
time.sleep(0.3)
>>>>>>> eda0b8139d6701d811c8445cfa7ff26a263f7d33
solve()
print(start_time)

