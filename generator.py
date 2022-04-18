# This is unfinished
import sudoku
from random import randint, random

class Generator(sudoku.Sudoku):

    def __init__(self):
        sudoku.Sudoku.__init__()
    
        self.__grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    
    def hints(self):
        hints = 0
        for row in range(9):
            for col in range(9):
                if self.__grid[row][col] != 0:
                    hints += 1
        return hints


    def generate(self):
        while self.hints() < 20:
            random_row = random.randint(0,8)
            random_column = random.randint(0,8)
            random_number = random.randint(1,9) 
            if sudoku.Sudoku.check_possible(random_row, random_column, random_number):
                self.__grid[random_row][random_column] = random_number

            print(self.__grid)