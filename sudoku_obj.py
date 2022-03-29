#class Board:

#    def __init__(self) -> None:
 #       pass

  #  def make:

   # def draw:
class Sudoku:

    def __init__(self):

        self.__board = self

    def make(self, difficulty):
        
        if difficulty == "easy":
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\easy\\easy_sudoku1.txt", "r")
        elif difficulty == "medium":
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\medium\\medium_sudoku1.txt", "r")
        else:
            file = open("C:\\Koulu\OOP\\sudoku_solver\\sudokus\\hard\\hard_sudoku1.txt", "r")
        board = []
        line = file.read()
        line = line.split("\n")
        for char in line:
            char = list(char)
            board.append(char)
        self.__board = board
        


    def draw(self):
        print("+" + "---+"*9)
        for i, row in enumerate(self.__board):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2:
                print("+" + "---+"*9)
            else:
                print("+" + "   +"*9)

    def solve(self):
        print("Solving sudoku...")


sudoku = Sudoku()
sudoku.make("easy")
sudoku.draw()
sudoku.solve()