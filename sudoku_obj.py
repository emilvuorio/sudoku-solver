
from random import randint, random
import time


class Sudoku:

    def __init__(self):
        
        self.__board = self

    def make_board(self, difficulty):

       # if difficulty == "easy":
        #    file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\easy\\easy_sudoku1.txt", "r")
        #elif difficulty == "medium":
         #   file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\medium\\medium_sudoku1.txt", "r")
        #else:
        #    file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\hard\\hard_sudoku1.txt", "r")
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

    
    def check_possible(self, row, column, n):
        for i in range(0,9):
            if self.__board[row][i] == n:
                return False
        for i in range(0,9):
            if self.__board[i][column] == n:
                return False
        
        column_square = (column // 3) * 3
        row_square = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.__board[row_square+i][column_square+j] == n:
                    return False
        return True
        



    def solve(self):
        for row in range(0,9):
            for cell in range(0,9):
                if self.__board[row][cell] == 0:
                    for n in range(1,10):
                        if self.check_possible(row,cell,n):
                            self.__board[row][cell] = n
                            #self.draw()
                            #time.sleep(0.3)
                            self.solve()
<<<<<<< HEAD
                            self.__board[y][x] = 0
                    return
                    
=======
                            self.__board[row][cell] = 0
                    return
        #self.draw()
        input()

class Generator(Sudoku):
    
    def __init__(self):
        super().__init__()
        self.__board = [[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]]
>>>>>>> 7ad2650042241a2cf9e0e7d793749a56a496ddee
        

    def generate(self):
        import random
        random_row = random.randint(0,8)
        random_column = random.randint(0,8)
        random_number = random.randint(1,9)
        
        self.__board[random_row][random_column] = random_number


        super(Generator, self).draw()


sudoku = Sudoku()
sudoku.make_board("easy")
sudoku.solve()
sudoku.draw()

generator = Generator()
generator.generate()
generator.draw()