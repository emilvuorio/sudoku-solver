from random import randint, random
import time
import pygame


class Sudoku:

    def __init__(self):
        
        self.__grid = self
        self.__background_color = (153, 204, 255)
        self.__highlighted_color = (100,100,100)
        self.__original_num_color = (0, 0, 0)
        self.__buffer = 5
        self.original_grid = self
        self.__font = pygame.font.SysFont('Comic Sans MS', 35)
        
        
    def make_grid(self):

        self.__grid  = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]
    
        self.__original_grid = [[self.__grid[row][col] for col in range(len(self.__grid[0]))] for row in range(len(self.__grid))]

    def check_possible(self,y, x, n):
        for i in range(0,9):
            if self.__grid[y][i] == n:
                return False
        for i in range(0,9):
            if self.__grid[i][x] == n:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.__grid[y0+i][x0+j] == n:
                    return False
        return True

def is_solved(self):

    for y in range(9):
        for x in range(9):
            if self.__grid[y][x] == 0:
                return False
    return True

def solve(self,screen):
    
    for y in range(9):
        for x in range(9):
            if self.__grid[y][x] == 0:
                for n in range(1,10):
                    if self.check_possible(y,x,n):
                        self.__grid[y][x] = n
                        pygame.draw.rect(screen, self.__background_color, ((x+1)*50 + self.__buffer, (y+1)*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        value = self.__font.render(str(n), True, (0,0,0))
                        screen.blit(value, ((x+1)*50 +15,(y+1)*50))
                        pygame.display.update()
                        pygame.time.delay(20)
                        solve(screen)
                        
                        if is_solved():
                            return

                        self.__grid[y][x] = 0
                        pygame.draw.rect(screen, self.__background_color, ((x+1)*50 + self.__buffer, (y+1)*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        pygame.display.update()
                return

def user_input(self,screen, position):
    row,col = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if(self.__original_sudoku[row-1][col-1] != 0):
                    return

                if(event.key == 48): 
                    self.__grid[row-1][col-1] = event.key - 48
                    pygame.draw.rect(screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                    pygame.display.update()
                    return

                if(0 < event.key - 48 <10):  
                    pygame.draw.rect(screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                    value = myfont.render(str(event.key-48), True, (0,100,0))
                    screen.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[row-1][col-1] = event.key - 48
                    pygame.display.update()
                    return
                return
    