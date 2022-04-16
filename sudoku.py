
from random import randint, random
import time
import pygame


class Sudoku:

    def __init__(self):
        pygame.init()
        self.__grid = self
        self.__original_grid = self
        self.__background_color = (153, 204, 255)
        self.__highlighted_color = (235, 12, 12)
        self.__original_num_color = (0, 0, 0)
        self.__buffer = 5
        self.__original_grid = self
        self.__fontsudoku = pygame.font.SysFont('Comic Sans MS', 35)
        self.__screen = pygame.display.set_mode((1000, 700))
        
        
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

    def check_possible(self,row, col, n):
        for i in range(0,9):
            if self.__grid[row][i] == n:
                return False
        for i in range(0,9):
            if self.__grid[i][col] == n:
                return False

        x0 = (col // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.__grid[y0+i][x0+j] == n:
                    return False
        return True

    def is_solved(self):

        for row in range(9):
            for col in range(9):
                if self.__grid[row][col] == 0:
                    return False
        return True

    def solve(self):
        
        for row in range(9):
            for col in range(9):
                if self.__grid[row][col] == 0:
                    for n in range(1,10):
                        if self.check_possible(row,col,n):
                            self.__grid[row][col] = n
                            pygame.draw.rect(self.__screen, self.__background_color, ((col+1)*50 + self.__buffer, (row+1)*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                            value = self.__fontsudoku.render(str(n), True, (0,0,0))
                            self.__screen.blit(value, ((col+1)*50 +15,(row+1)*50))
                            pygame.display.update()
                            pygame.time.delay(20)
                            self.solve()
                            
                            if self.is_solved():
                                return

                            self.__grid[row][col] = 0
                            pygame.draw.rect(self.__screen, self.__background_color, ((col+1)*50 + self.__buffer, (row+1)*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                            pygame.display.update()
                    return


    def user_input(self, position):
        row,col = position[1], position[0]
        
        while True:
            pygame.draw.rect(self.__screen, self.__highlighted_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    
                    if(self.__original_grid[row-1][col-1] != 0):
                        return

                    if(event.key == 48): 
                        self.__grid[row-1][col-1] = event.key - 48
                        pygame.draw.rect(self.__screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        pygame.display.update()
                        return

                    if(0 < event.key - 48 <10):  
                        pygame.draw.rect(self.__screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        value = self.__fontsudoku.render(str(event.key-48), True, (0,100,0))
                        self.__screen.blit(value, (position[0]*50 +15, position[1]*50))
                        self.__grid[row-1][col-1] = event.key - 48
                        pygame.display.update()
                        return
                    return

    def reset_grid(self):

        for row in range(0, len(self.__grid[0])):
            for col in range(0, len(self.__grid[0])):
                if self.__grid[row][col] != self.__original_grid[row][col]:
                    self.__grid[row][col] = 0
        pygame.display.update()

    def populate(self):


        for row in range(0, len(self.__grid[0])):
            for col in range(0, len(self.__grid[0])):
                if(0<self.__grid[row][col]<10):
                    value = self.__fontsudoku.render(str(self.__grid[row][col]), True, self.__original_num_color)
                    self.__screen.blit(value, ((col+1)*50 + 15, (row+1)*50 ))
        pygame.display.update()
            


    def start_game(self):

        pygame.init()
        
        icon = pygame.image.load("sudoku_icon.png")
        pygame.display.set_icon(icon)
        self.__screen.fill((153, 204, 255))
        
        # draw lines
        for i in range(0,10):
            if(i%3 == 0):
                pygame.draw.line(self.__screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                pygame.draw.line(self.__screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

            pygame.draw.line(self.__screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
            pygame.draw.line(self.__screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
        self.populate()
                
        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                    pos = pygame.mouse.get_pos()
                    
                    self.user_input((pos[0]//50, pos[1]//50))

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if self.is_solved():
                            return
                        self.reset_grid()
                        self.populate()
                        self.solve()


class Generator(Sudoku):

    def __init__(self):
        Sudoku.__init__()


sudoku = Sudoku()
sudoku.make_grid()
sudoku.start_game()