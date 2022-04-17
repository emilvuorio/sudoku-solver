from sudoku import self
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

    def generate(self):
        for i in range(20):
            random_row = random.randint(0,8)
            random_column = random.randint(0,8)
            if [random_row][random_column] == 0:
                for n in range(10):
                    random_number = random.randint(1,9) 
                    if sudoku.Sudoku.check_possible(random_row, random_column, random_number):
                        self.__grid[random_row][random_column] = random_number