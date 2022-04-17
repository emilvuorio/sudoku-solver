# main_menu.py
# Authors Emil Vuorio and Iliyan Kichukov
# Main menu for sudoku game

import pygame

<<<<<<< HEAD
=======
def launch(player): 
        import sudoku
        sudoku_game = sudoku.Sudoku(player)
        sudoku_game.start_game()
>>>>>>> 94c255e09f021d0cc85f435eb0f5ab5e6f3dc5eb

pygame.init()

font = pygame.font.SysFont("Comic Sans MS", 35)
font2 = pygame.font.SysFont("Comic Sans MS", 25)
menu_screen = pygame.display.set_mode((1000, 700))

def draw_menu_text(text, font, color, surface, horizontal, vertical):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (horizontal, vertical)
    surface.blit(textobj, textrect)

def launch_game(player):
    
    sudokugame = sudoku.Sudoku(player)
    sudokugame.make_grid()
    sudokugame.start_game()


def main():

    pygame.display.set_caption('Sudoku Main Menu')
    while True:
        menu_screen.fill((255,255,255))
        menu_background = pygame.image.load("main_menu_background3.png")
        menu_screen.blit(menu_background, (0, 0))
        draw_menu_text("Sudoku game MAIN MENU", font, (255,255,255), menu_screen, 15,20)
        draw_menu_text("Choose player:", font2, (255,255,255), menu_screen, 15,130)
        player1_button = pygame.Rect(15, 200, 80, 50)
        player2_button = pygame.Rect(100, 200, 100, 50)
        quit_button = pygame.Rect(15, 500, 105, 50)

        m_horizontal, m_vertical = pygame.mouse.get_pos()

        pygame.draw.rect(menu_screen, (255, 204, 0), player1_button)
        pygame.draw.rect(menu_screen, (144, 238, 144), player2_button)
        pygame.draw.rect(menu_screen, (255, 0, 0), quit_button)

        menu_screen.blit(font.render('Emil', True, (255,255,255)), (15, 200))
        menu_screen.blit(font.render('Iliyan', True, (255,255,255)), (100, 200))
        menu_screen.blit(font.render('QUIT', True, (255,255,255)), (15, 500))


        draw_menu_text("Part of the TUAS OOP course", font2, (255,255,255), menu_screen, 550,330)
        draw_menu_text("Authors: Iliyan Kichukov and Emil Vuorio", font2, (255,255,255), menu_screen, 500,430)

        if player1_button.collidepoint((m_horizontal, m_vertical)):
<<<<<<< HEAD
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                
                launch_game("Emil")
        if player2_button.collidepoint((m_horizontal, m_vertical)):
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                launch_game("Iliyan")
=======
            if click:
                launch("Emil")
        if player2_button.collidepoint((m_horizontal, m_vertical)):
            if click:
                launch("Iliyan")
>>>>>>> 94c255e09f021d0cc85f435eb0f5ab5e6f3dc5eb
        if quit_button.collidepoint((m_horizontal, m_vertical)):
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
   
        pygame.display.update()
        

main()