import enum
from re import X


class Sudoku:

    def __init__(self):

        self.__board = self

    def make_board(self, difficulty):

        if difficulty == "easy":
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\easy\\easy_sudoku1.txt", "r")
        elif difficulty == "medium":
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\medium\\medium_sudoku1.txt", "r")
        else:
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\hard\\hard_sudoku1.txt", "r")
        board = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
        #board_f = file.read()
        #board_f = board_f.split("\n") #split the rows with enter
        #for line in board_f: #
         #   line = list(line) #makes a line to a list
          #  for n, i in enumerate(line): # loops through line, converts to int
           #     line[n] = int(i)
           # board.append(line)
        self.__board = board
        
        


    def draw(self):
        # fancy way to make sudoku pretty
        print("+" + "---+"*9)
        for i, row in enumerate(self.__board):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2:
                print("+" + "---+"*9)
            else:
                print("+" + "   +"*9)


        # jotain testailua kello 23:17 yöllä


    
    def check_possible(self, y, x, n):
        for i in range(0,9):
            if self.__board[y][i] == n:
                return False
        for i in range(0,9):
            if self.__board[i][x] == n:
                return False
        
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.__board[y0+i][x0+j] == n:
                    return False
        return True
        



    def solve(self):
        for y in range(0,9):
            for x in range(0,9):
                if self.__board[y][x] == 0:
                    for n in range(1,10):
                        if self.check_possible(y,x,n):
                            self.__board[y][x] = n
                            self.draw()
                            self.solve()
                            self.__board[y][x] = 0
                    return 
        

sudoku = Sudoku()
sudoku.make_board("easy")
sudoku.solve()
sudoku.draw()