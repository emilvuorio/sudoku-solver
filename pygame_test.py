import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load("sudoku_icon.png")
pygame.display.set_icon(icon)

sudoku = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def draw_sudoku(sudoku):
        print("+" + "---+"*9)
        for i, row in enumerate(sudoku):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2:
                print("+" + "---+"*9)
            else:
                print("+" + "   +"*9)

#Sudoku = pygame.draw_sudoku(sudoku)
#sudokuX = 200
#sudokuY = 200

#def soudouku():
 #   screen.blit(Sudoku, (sudokuX, sudokuY))

while True:
    screen.fill((153, 204, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #soudouku()
    pygame.display.update()
    draw_sudoku(sudoku)