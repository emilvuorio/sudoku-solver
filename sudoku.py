# sudoku.py
# Authors Emil Vuorio and Iliyan Kichukov
# sudoku class




import sys
import player_class
import pygame


class Sudoku:

    def __init__(self, player):
        pygame.init()
        self.__grid = self
        self.__original_grid = self
        
        self.__original_num_color = (0, 0, 0)
        self.__buffer = 5

        self.__start_time = int(pygame.time.get_ticks() / 1000)
        self.__fontsudoku = pygame.font.SysFont('Comic Sans MS', 35)
        self.__screen = pygame.display.set_mode((1000, 700))

        if player == "Emil":
            self.__player = player_class.Emil()

        elif player == "Iliyan":
            self.__player = player_class.Iliyan()
        self.__background_color = self.__player.get_fav_color()
        self.__highlighted_color = (self.__background_color[0] * 0.8, self.__background_color[1] * 0.8, self.__background_color[2] * 0.8)

         
        
        
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

        # Creates a copy of a grid for later comparassion
        self.__original_grid = [[self.__grid[row][col] for col in range(len(self.__grid[0]))] for row in range(len(self.__grid))]


    def check_possible(self,row, col, n):

        # Loops through all the rows
        for i in range(0,9):    
            if self.__grid[row][i] == n:
                return False
        # Loops through all the colls
        for i in range(0,9):
            if self.__grid[i][col] == n:
                return False
        # Loops through 3 x 3 Cubes 
        col_cube = (col // 3) * 3
        row_cube = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.__grid[row_cube+i][col_cube+j] == n:
                    return False

        return True

    def is_solved(self):

        for row in range(9):
            for col in range(9):
                if self.__grid[row][col] == 0:
                    return False
        return True

    def solve(self):
        # Function loops through all the squares in sudoku
        # When empty square is found it loops through the numbers to see if they fit
        # It enters first possible number and starts recursion stack
        # When there's no possible numbers to add it backtracks back, resets numbers back to 0 and tries next possible number
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
        # get positions
        row,col = position[1], position[0]
        
        while True:
            self.display_score()
            # Highlights clicked square
            if(self.__original_grid[row-1][col-1] == 0):
                pygame.draw.rect(self.__screen, self.__highlighted_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                pygame.display.update()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return

                
                

                if event.type == pygame.KEYDOWN:
                    
                    # If the square is hard coded number
                    if(self.__original_grid[row-1][col-1] != 0):
                        return
                    
                    # 0's ascii value is 48
                    if(event.key == 48):
                        
                        
                        self.__grid[row-1][col-1] = event.key - 48
                        pygame.draw.rect(self.__screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        pygame.display.update()
                        return

                    # number between 1 and 9 draws new value

                    if(0 < event.key - 48 <10):  
                        pygame.draw.rect(self.__screen, self.__background_color, (position[0]*50 + self.__buffer, position[1]*50+ self.__buffer,50 -2*self.__buffer , 50 - 2*self.__buffer))
                        value = self.__fontsudoku.render(str(event.key-48), True, (0,100,0))
                        self.__screen.blit(value, (position[0]*50 +15, position[1]*50))
                        self.__grid[row-1][col-1] = event.key - 48
                        pygame.display.update()
                        return
                    return

    def reset_grid(self):
    
        # Compares current grid to original grid 
        for row in range(0, len(self.__grid[0])):
            for col in range(0, len(self.__grid[0])):
                if self.__grid[row][col] != self.__original_grid[row][col]:
                    self.__grid[row][col] = 0
        pygame.display.update()

    def populate(self):
        # Populates drawn sudoku with numbers

        for row in range(0, len(self.__grid[0])):
            for col in range(0, len(self.__grid[0])):
                if(0<self.__grid[row][col]<10):
                    value = self.__fontsudoku.render(str(self.__grid[row][col]), True, self.__original_num_color)
                    self.__screen.blit(value, ((col+1)*50 + 15, (row+1)*50 ))
        pygame.display.update()

    def draw_lines(self):

        # draw lines
        for i in range(0,10):
            if(i%3 == 0):
                pygame.draw.line(self.__screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                pygame.draw.line(self.__screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

            pygame.draw.line(self.__screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
            pygame.draw.line(self.__screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
            
    def display_score(self):
        # Redraws score
        self.__screen.fill(self.__background_color, (520,30, 160, 50))
        current_time = int(pygame.time.get_ticks() / 1000) - self.__start_time
        score_surf = self.__fontsudoku.render(f'Time: {current_time}',False,(64,64,64))
        score_rect = score_surf.get_rect(center = (600,65))
        self.__screen.blit(score_surf,score_rect)

        return current_time
        
        
    def start_game(self):

        pygame.init()
        
        
        pygame.display.set_caption('Sudoku')
        icon = pygame.image.load("sudoku_icon.png")
        pygame.display.set_icon(icon)

        self.__screen.fill((self.__background_color))
        self.draw_lines()
        self.populate()


        hint_text = self.__fontsudoku.render("Press Space to give up", True, self.__original_num_color )
 
        # create a rectangular object for the
        # text surface object
        hint_rect = hint_text.get_rect()
        hint_rect.midleft = (520, 160)
        self.__screen.blit(hint_text, hint_rect)
        player_name = self.__player.get_player_name()
        player_playing_text =  self.__fontsudoku.render("Player playing " + player_name, True, self.__original_num_color)
        player_playing_rect = player_playing_text.get_rect()
        player_playing_rect.midleft = (520, 240)
        self.__screen.blit(player_playing_text, player_playing_rect)
        
        
        pygame.display.update()
        
        player_playing = True

        
        

        
        while True:
            
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                    pos = pygame.mouse.get_pos()
                    
                    self.user_input((pos[0]//50, pos[1]//50))

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_playing = False
                        self.__screen.fill(self.__background_color, (520,30, 160, 60))
                        if self.is_solved():
                            return
                        self.reset_grid()
                        self.populate()
                        self.solve()

            if player_playing:
                self.display_score()
            
            if self.is_solved and player_playing:

                score = self.display_score()
                
                if int(self.__player.get_highscore()) > score:
                    self.__player.set_highscore(score)

            pygame.display.update()
            