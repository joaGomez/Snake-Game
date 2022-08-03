from gameModesAndExtra import *


#----------------------------------------------------------------------------


class Menu:

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.menu_value = None
        self.mouse_x = -1
        self.mouse_y = -1
        self.mouse_pressed = False
        self.state = True

        self.gameModes = GameModes(self.screen, self.font)

        self.logo = pygame.image.load(os.path.join('Snake_Game\Imagenes', 'logo_snake.jpg'))
        self.keyboard_input = pygame.image.load(os.path.join('Snake_Game\Imagenes', 'key_menu2.png'))

    def printData(self):
        self.screen.fill(WHITE)

        title = self.font.render("Keyboard options", True, BLACK)
        self.screen.blit(title, (250, 50))
        
        go_back = self.font.render("Go back", True, BLACK)
        self.screen.blit(go_back, (300, 570))

        self.screen.blit(self.keyboard_input, (10, 90))

        pygame.display.flip()

    def moreInfo(self):
        self.printData()
        
        menu_value = CONTINUE_VALUE
        mouse_pressed = False
        x = y = -1
        
        state = True
        
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
                    menu_value = EXIT_GAME_VALUE
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                    mouse_pressed = True
                    x, y = pygame.mouse.get_pos()
                    
            if mouse_pressed:
                if inside(x, y, 297, 567, 75, 30):
                    state = False
                        
                mouse_pressed = False
                
        return menu_value



    def menuOptions(self):
        self.screen.fill(WHITE)

        self.screen.blit(self.logo, (-50, -100))

        title = self.font.render("SNAKE GAME.py", True, BLACK)
        self.screen.blit(title, (250, 320))

        start_game = self.font.render("Start", True, BLACK)
        self.screen.blit(start_game, (295, 390))

        game_modes = self.font.render("Game modes", True, BLACK)
        self.screen.blit(game_modes, (265, 450))

        more_game = self.font.render("More", True, BLACK)
        self.screen.blit(more_game, (295, 510))

        exit_game = self.font.render("Exit", True, BLACK)
        self.screen.blit(exit_game, (300, 580))

        pygame.display.flip()


    def mainMenu(self):


        while self.state:

            self.menuOptions()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = False
                    self.menu_value = EXIT_GAME_VALUE

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                    self.mouse_pressed = True
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()



            if self.mouse_pressed:
                if inside(self.mouse_x, self.mouse_y, 295, 390, 35, 25):
                    self.menu_value = CONTINUE_VALUE
                    self.state = False

                if inside(self.mouse_x, self.mouse_y, 265, 450, 115, 25):
                    if self.gameModes.selectGameMode() == EXIT_GAME_VALUE:
                        self.state = False
                        self.menu_value = EXIT_GAME_VALUE

                if inside(self.mouse_x, self.mouse_y, 295, 505, 40, 30):
                    if self.moreInfo() == EXIT_GAME_VALUE:
                        self.state = False
                        self.menu_value = EXIT_GAME_VALUE


                if inside(self.mouse_x, self.mouse_y, 300, 575, 35, 30):
                    self.state = False
                    self.menu_value = EXIT_GAME_VALUE

                self.mouse_pressed = False

        return self.menu_value





#----------------------------------------------------------------------------


class PauseMenu:

    def __init__(self, screen, font):
        self.screen = screen
        self.pause_value = None
        self.font = font
        self.state = True
        self.mouse_x = -1
        self.mouse_y = -1
        self.mouse_pressed = False

    def restartMenuValues(self):        # TODO: Change name of function     -> validate if necessary function
        self.pause_value = None
        self.state = True
        self.mouse_x = -1
        self.mouse_y = -1

    def options(self):
        self.screen.fill(BLACK)

        continue_ = pygame.Rect(160, 170, 320, 50)
        pygame.draw.rect(self.screen, RED, continue_, 2)
        continue_txt = self.font.render("CONTINUE", True, RED)
        self.screen.blit(continue_txt, (270, 185))

        exit_menu = pygame.Rect(160, 270, 320, 50)
        pygame.draw.rect(self.screen, RED, exit_menu, 2)
        exit_txt = self.font.render("EXIT TO MENU", True, RED)
        self.screen.blit(exit_txt, (260, 285))

        exit_ = pygame.Rect(160, 370, 320, 50)
        pygame.draw.rect(self.screen, RED, exit_, 2)
        exit_game_txt = self.font.render("EXIT GAME", True, RED)
        self.screen.blit(exit_game_txt, (270, 385))

        pygame.display.flip()


    def pause(self):

        self.options()      # Print options on screen

        while self.state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = False
                    self.pause_value = EXIT_GAME_VALUE

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                    self.mouse_pressed = True

            if self.mouse_pressed:
                if inside(self.mouse_x, self.mouse_y, 160, 170, 320, 50): # Continue button
                    self.state = False
                    self.pause_value = CONTINUE_VALUE

                if inside(self.mouse_x, self.mouse_y, 160, 270, 320, 50): # Exit to menu button
                    self.state = False
                    self.pause_value = EXIT_TO_MENU_VALUE

                if inside(self.mouse_x, self.mouse_y, 160, 370, 320, 50): # Exit game button
                    self.state = False
                    self.pause_value = EXIT_GAME_VALUE

        return self.pause_value

    def playingOptions(self):
        self.screen.fill(BLACK)

        restartGame_msj = self.font.render("Do you want to continue playing?", True, (WHITE))
        self.screen.blit(restartGame_msj, (180, 200))

        yes_msj = self.font.render("YES", True, (WHITE))
        self.screen.blit(yes_msj, (250, 300))

        no_msj = self.font.render("NO", True, (WHITE))
        self.screen.blit(no_msj, (360, 300))

        pygame.display.flip()

    def restartGame(self):  # TODO

        self.playingOptions()

        chosen_option = None

        self.state = True

        while self.state:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = False
                    chosen_option = EXIT_GAME_VALUE

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                    self.mouse_pressed = True

                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

            if inside(self.mouse_x, self.mouse_y, 250, 300, 50, 25):        # Continue playing
                pygame.draw.line(self.screen, WHITE, (255, 325), (280, 325))
                pygame.display.flip()

            elif inside(self.mouse_x, self.mouse_y, 360, 300, 50, 25):      # Exit game
                pygame.draw.line(self.screen, WHITE, (360, 325), (385, 325))
                pygame.display.flip()

            else:
                self.playingOptions()

            if self.mouse_pressed:
                if inside(self.mouse_x, self.mouse_y, 250, 300, 50, 25):        # Continue playing
                    self.state = False
                    chosen_option = EXIT_TO_MENU_VALUE

                elif inside(self.mouse_x, self.mouse_y, 360, 300, 50, 25):      # Exit game
                    self.state = False
                    chosen_option = EXIT_GAME_VALUE

        return chosen_option        # Returns decision, either continue player or exit game




#----------------------------------------------------------------------------
