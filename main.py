
def draw_sudoku(sudoku):


    #line = "-------"



  #  for n,row in enumerate(sudoku):
        
   #     if n % 3 == 0:
    #        print(line *2)
     #   for n, c in enumerate(row):

      #      if n % 3 == 0:
       #         print("|", end="")
        #    if n < 8:
         #       print(c, end="")
          #  else:
           #     print(c, "|")
        


    print("+" + "---+"*9)
    for i, row in enumerate(sudoku):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

def check_not_hard_coded(hard_coded_numbers, row_and_cell):

    for x in hard_coded_numbers:
        if x == row_and_cell:
            return True
    return False


#def create sudoku

sudoku = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

hard_coded_numbers = []

for row_n, row in enumerate(sudoku):

    for cell_n, cell in enumerate(row):
         if sudoku[row_n][cell_n] != 0:

            hard_number = row_n, cell_n
            hard_coded_numbers.append(hard_number)
            #print(sudoku[row_n][cell_n])
while True:
    draw_sudoku(sudoku)


    row_to_change = int(input("Input row number you want to change: "))
    cell_to_change = int(input("Input cell numbere what you want to change: "))
    new_number = int(input("Input new number: "))
    row_and_cell = tuple((row_to_change, cell_to_change))

    hard_coded = check_not_hard_coded(hard_coded_numbers, row_and_cell)

    if hard_coded:

        print("You can't replace hard coded number.")


    else:

        for n, row in enumerate(sudoku):

            if n == row_to_change:
                sudoku[n][cell_to_change] = new_number



