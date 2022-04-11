from distutils.log import set_threshold
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((1000, 700))
icon = pygame.image.load("sudoku_icon.png")
pygame.display.set_icon(icon)
background_color = (0, 0, 0)


sudoku = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
    

font1 = pygame.font.SysFont("Comic Sans MS", 35)
font2 = pygame.font.SysFont("Comic Sans MS", 20)

row_text=""
grid_text=""
numberext=""
row_input = pygame.Rect(50, 50, 100, 32)
grid_input = pygame.Rect(100,50,50,32)
number_input=pygame.Rect(150,70,50, 32)

screen.fill((153, 204, 255))


color_active = pygame.Color('green')
color_passive = pygame.Color('green')
color = color_passive

for i in range(0,10):
    if (i%3 == 0  ):
        pygame.draw.line(screen, (0,0,0), (50 + 50*i,50),(50 + 50*i, 500),4)
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i),(500, 50 + 50*i),4)
    pygame.draw.line(screen, (0,0,0), (50 + 50*i ,50),(50 + 50*i, 500),2)
    pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i),(500, 50 + 50*i),2)
pygame.display.update()

for i in range (0, len(sudoku[0])):
    for j in range (0, len(sudoku[0])):
        if (0<sudoku[i][j]<10):
            value = font1.render(str(sudoku[i][j]), True, background_color)
            screen.blit(value, ((j+1)*50 +15, (i+1)*50))
pygame.display.update()

active = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if row_input.collidepoint(event.pos):
                active == True
            else:
                active = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:9]

            else:
                row_text += event.unicode

    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, row_input)
    user_text = font2.render(row_text, True, (255, 255, 255))
    screen.blit(user_text, (row_input.x+5, row_input.y+5))
    row_input.w = max(100, user_text.get_width()+10)
    pygame.display.flip()
    pygame.display.update()