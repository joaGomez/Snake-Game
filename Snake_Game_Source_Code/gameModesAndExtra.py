from constants import *


def inside(x, y, left, top, width, height):     # devuelve true si esta dentro de los parametros
    if  x >= left and x <= left + width and y >= top and y <= top + height:
        return True
    else:
        return False


#---------------------------------------------------------------

class GameModes:
    
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.limitless = False
        self.endless = False
        
        self.state = True
        self.value = None
        self.mouse_pressed = False
        self.mouse_x = -1
        self.mouse_y = -1
    
    def drawGameModes(self):
        self.screen.fill(BLACK)
        
        title = self.font.render("SELECT ANY MODE", True, GREY)
        self.screen.blit(title, (230, 50))
        
        soon = self.font.render("More will be added soon...", True, GREY)
        self.screen.blit(soon, (220, 360))
        
        back = self.font.render("Go back", True, GREY)
        self.screen.blit(back, (290, 550))
        
        if self.endless == True:
            endless = self.font.render("ENDLESS", True, GREEN)
            self.screen.blit(endless, (150, 200))
            
        elif self.endless == False:
            endless = self.font.render("ENDLESS", True, GREY)
            self.screen.blit(endless, (150, 200))
            
        if self.limitless == True:
            limitless = self.font.render("LIMITLESS", True, GREEN)
            self.screen.blit(limitless, (400, 200))
            
        elif self.limitless == False:
            limitless = self.font.render("LIMITLESS", True, GREY)
            self.screen.blit(limitless, (400, 200))
        
        pygame.display.flip()
        
    
    def selectGameMode(self):
        
        self.state = True       # Reset values for every time the user enters this menu
        self.value = None
        
        while self.state:
            
            self.drawGameModes()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.value = EXIT_GAME_VALUE
                    self.state = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                    self.mouse_pressed = True
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            
            if self.mouse_pressed:
                if inside(self.mouse_x, self.mouse_y, 150, 195, 80, 30):
                    if self.endless:
                        self.endless = False    # If it was previously selected, it deselects
                    else:
                        self.endless = True
                
                if inside(self.mouse_x, self.mouse_y, 400, 195, 90, 30):
                    if self.limitless:
                        self.limitless = False    # If it was previously selected, it deselects
                    else:
                        self.limitless = True
                        
                if inside(self.mouse_x, self.mouse_y, 290, 545, 65, 30):
                    self.state = False
                    self.value = CONTINUE_VALUE
                
                self.mouse_pressed = False
            
            
        return self.value