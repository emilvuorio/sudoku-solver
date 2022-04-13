import pygame

background_color = (153, 204, 255)
highlighted_color = (100,100,100)
original_num_color = (0, 0, 0)
buffer = 5

grid  = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]


original_sudoku = [[grid[row][col] for col in range(len(grid[0]))] for row in range(len(grid))]



def user_input(screen, position):
    row,col = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if(original_sudoku[row-1][col-1] != 0):
                    return

                if(event.key == 48): 
                    grid[row-1][col-1] = event.key - 48
                    pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return

                if(0 < event.key - 48 <10):  
                    pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,100,0))
                    screen.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[row-1][col-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def check_possible(y, x, n):
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def is_solved():

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                return False
    return True

def solve(screen):
    font = pygame.font.SysFont('Comic Sans MS', 35)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if check_possible(y,x,n):
                        grid[y][x] = n
                        pygame.draw.rect(screen, background_color, ((x+1)*50 + buffer, (y+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = font.render(str(n), True, (0,0,0))
                        screen.blit(value, ((x+1)*50 +15,(y+1)*50))
                        pygame.display.update()
                        #pygame.time.delay(25)
                        solve(screen)
                        
                        if is_solved():
                            return

                        grid[y][x] = 0
                        pygame.draw.rect(screen, background_color, ((x+1)*50 + buffer, (y+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                return
    

def reset_grid():

    for x in range(0, len(grid[0])):
        for y in range(0, len(grid[0])):
            if grid[x][y] != original_sudoku[x][y]:
                grid[x][y] = 0
    pygame.display.update()

def populate(screen, font):

    grid  = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = font.render(str(grid[i][j]), True, original_num_color)
                screen.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
            


def main():

    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    icon = pygame.image.load("sudoku_icon.png")
    pygame.display.set_icon(icon)
    screen.fill((153, 204, 255))
    font2 = pygame.font.SysFont('Comic Sans MS', 35)
    # draw lines
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    populate(screen,font2)
            
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                user_input(screen, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if is_solved():
                        return
                    reset_grid()
                    populate(screen, font2)
                    solve(screen)
   
main()