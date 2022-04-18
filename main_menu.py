# main_menu.py
# Authors Emil Vuorio and Iliyan Kichukov
# Main menu for sudoku game

import pygame
import sudoku


class Menu:
    
    def __init__(self):
        pygame.init()

        self.__font = pygame.font.SysFont("Comic Sans MS", 35)
        self.__font2 = pygame.font.SysFont("Comic Sans MS", 25)
        self.__menu_screen = pygame.display.set_mode((1000, 700))

    def draw_menu_text(self, text, font, color, surface, horizontal, vertical):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (horizontal, vertical)
        surface.blit(textobj, textrect)

    def launch_game(self,player):
        
        sudokugame = sudoku.Sudoku(player)
        sudokugame.make_grid()
        sudokugame.start_game()


    def main_menu(self):

        pygame.display.set_caption('Sudoku Main Menu')
        while True:
            self.__menu_screen.fill((255,255,255))
            menu_background = pygame.image.load("main_menu_background3.png")
            self.__menu_screen.blit(menu_background, (0, 0))
            self.draw_menu_text("Sudoku game MAIN MENU", self.__font, (255,255,255), self.__menu_screen, 15,20)
            self.draw_menu_text("Choose player:", self.__font2, (255,255,255), self.__menu_screen, 15,130)
            player1_button = pygame.Rect(15, 200, 80, 50)
            player2_button = pygame.Rect(100, 200, 100, 50)
            quit_button = pygame.Rect(15, 500, 105, 50)

            m_horizontal, m_vertical = pygame.mouse.get_pos()

            pygame.draw.rect(self.__menu_screen, (255, 204, 0), player1_button)
            pygame.draw.rect(self.__menu_screen, (144, 238, 144), player2_button)
            pygame.draw.rect(self.__menu_screen, (255, 0, 0), quit_button)

            self.__menu_screen.blit(self.__font.render('Emil', True, (255,255,255)), (15, 200))
            self.__menu_screen.blit(self.__font.render('Iliyan', True, (255,255,255)), (100, 200))
            self.__menu_screen.blit(self.__font.render('QUIT', True, (255,255,255)), (15, 500))


            self.draw_menu_text("Part of the TUAS OOP course", self.__font2, (255,255,255), self.__menu_screen, 550,330)
            self.draw_menu_text("Authors: Iliyan Kichukov and Emil Vuorio", self.__font2, (255,255,255), self.__menu_screen, 500,430)

            if player1_button.collidepoint((m_horizontal, m_vertical)):
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    return "Emil"
            if player2_button.collidepoint((m_horizontal, m_vertical)):
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.launch_game("Iliyan")
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
            
menu = Menu()
menu.main_menu()