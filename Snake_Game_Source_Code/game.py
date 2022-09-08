from menu import *




def isANewHighscore(score):
    file = open('Highscores.txt', 'r')
    readfile = file.readlines()
    
    state = False
    
    if len(readfile) != 0:
        highscores = []
        for line in readfile:
            score1, score2, score3, score4, score5 = line.split(",")
            highscores.append(int(score1))
            highscores.append(int(score2))
            highscores.append(int(score3))
            highscores.append(int(score4))
            highscores.append(int(score5))
            
        highscores.sort(reverse=True)
        
        if score > highscores[4]:
            highscores.remove(highscores[4])
            highscores.append(score)
            state = True
        
        highscores.sort(reverse=True)
        
        new_highscores = ''
        
        for i in range(0, len(highscores)):
            new_highscores += str(highscores[i])
            if i != 4:
                new_highscores += ','
        
        file = open('Highscores.txt', 'w')
        file.write(new_highscores)
        
    else:
        file = open('Highscores.txt', 'w')
        file.write('0,0,0,0,0')
        
    return state


def printHighScores(screen, score):
    
    is_highscore = isANewHighscore(int(score))
    
    file = open('Highscores.txt', 'r')
    readfile = file.readlines()
    
    highscores = []
    for line in readfile:
        score1, score2, score3, score4, score5 = line.split(",")
        highscores.append(int(score1))
        highscores.append(int(score2))
        highscores.append(int(score3))
        highscores.append(int(score4))
        highscores.append(int(score5))
        
    highscores.sort(reverse=True)
    
    screen.fill(BLACK)
    
    title_font = pygame.font.Font(os.path.join('Snake_Game_Source_Code/Fuentes', '256BYTES.TTF'), 40)
    
    cont = pygame.font.Font(None, 20)
    
    title = title_font.render("HIGHSCORES", True, YELLOW)
    screen.blit(title, (250, 50))
    
    continue_game = cont.render("continue", True, YELLOW)
    screen.blit(continue_game, (560, 620))
    
    score1 = title_font.render("1st: " + str(highscores[0]) + " pts", True, YELLOW)
    screen.blit(score1, (255, 150))
    
    score2 = title_font.render("2nd: " + str(highscores[1]) + " pts", True, YELLOW)
    screen.blit(score2, (255, 230))
    
    score3 = title_font.render("3rd: " + str(highscores[2]) + " pts", True, YELLOW)
    screen.blit(score3, (255, 310))
    
    score4 = title_font.render("4th: " + str(highscores[3]) + " pts", True, YELLOW)
    screen.blit(score4, (255, 390))
    
    score5 = title_font.render("5th: " + str(highscores[4]) + " pts", True, YELLOW)
    screen.blit(score5, (255, 470))
    
    if is_highscore:
        game_score = title_font.render("YOU SET A NEW RECORD!", True, YELLOW)
        screen.blit(game_score, (160, 550))
    
    else:
        game_score = title_font.render("MAYBE NEXT TIME...", True, RED)
        screen.blit(game_score, (210, 550))
    
    
    pygame.display.flip()
    
    state = True
    value = CONTINUE_VALUE
    mouse_pressed = False
    mouse_x = mouse_y = -1
    
    while state:   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
                value = EXIT_GAME_VALUE
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Detects mouse activity
                mouse_pressed = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
        if mouse_pressed:
            if inside(mouse_x, mouse_y, 555, 615, 65, 50):
                value = CONTINUE_VALUE
                state = False
            
            mouse_pressed = False
                
    return value
    
    
    
    
    

#----------------------------------------------------------------------------


class SnakeNodes:
    def __init__(self, index, position_x, position_y):
        self.index = index
        self.position_x = position_x
        self.position_y = position_y
        self.prev = None
        self.next = None
        

#----------------------------------------------------------------------------


class DoublyLinkedList:
    def __init__(self, position_x, position_y):
        self.snake_head = SnakeNodes(0, position_x, position_y)           # Snake head -> index = 0 / Start of the snake body
        
    def add(self, snake):
        last_node = self.snake_head
        count = 1
        
        while last_node.next != None:
            last_node = last_node.next
            count += 1
        
        if snake.direction == 'left':
            position_x = last_node.position_x + 16
            position_y = last_node.position_y
        elif snake.direction == 'right':
            position_x = last_node.position_x - 16
            position_y = last_node.position_y
        elif snake.direction == 'up':
            position_x = last_node.position_x
            position_y = last_node.position_y - 16
        elif snake.direction == 'down':
            position_x = last_node.position_x
            position_y = last_node.position_y + 16
        
        
        new_node = SnakeNodes(count, position_x, position_y)
        last_node.next = new_node
        new_node.prev = last_node
        
    def delete(self, index):
        last_node = self.snake_head
        
        while last_node.next != None:
            last_node = last_node.next
        
        while index <= last_node.index:
            last_node = last_node.prev
            #del last_node.next
        last_node.next = None
        

#----------------------------------------------------------------------------


class Snake:
    
    def __init__(self, screen, movement_speed):
        self.screen = screen
        self.movement_speed = movement_speed
        self.snake_color = GREEN
        self.snake_body = DoublyLinkedList(START_POSITION_PLAYER[0], START_POSITION_PLAYER[1])
        self.direction = None
        self.size = 16      # Size in pixels for every square of the snake body
        self.life = 'alive'
        self.endless_mode = False
        self.limitless_mode = False
        
    def draw(self):
        
        node = self.snake_body.snake_head
        pygame.draw.rect(self.screen, (self.snake_color), ((node.position_x, node.position_y), (self.size, self.size)))
        pygame.draw.rect(self.screen, BLACK, (node.position_x, node.position_y, self.size, self.size), 1)
        
        while node.next != None:
            node = node.next
            pygame.draw.rect(self.screen, (self.snake_color), ((node.position_x, node.position_y), (self.size, self.size)))
            pygame.draw.rect(self.screen, BLACK, (node.position_x, node.position_y, self.size, self.size), 1)
        
        pygame.display.flip()
    
    def detectCollision(self):
        snake_head = self.snake_body.snake_head
        next_node = snake_head.next
        while next_node != None:
            if snake_head.position_x == next_node.position_x and snake_head.position_y == next_node.position_y:
                if self.endless_mode:
                    self.snake_body.delete(next_node.index)
                else:
                    self.life = 'dead'
                break
            
            next_node = next_node.next
    
    def eatFruit(self, fruit):
        return self.snake_body.snake_head.position_x == (fruit.position_x) and self.snake_body.snake_head.position_y == (fruit.position_y)
           
    
    def move(self):
        
        if self.direction != None:
            last_node = self.snake_body.snake_head
            
            while last_node.next != None:
                last_node = last_node.next
            
            
            while last_node.prev != None:
                prev_node = last_node.prev
                last_node.position_x = prev_node.position_x
                last_node.position_y = prev_node.position_y
                last_node = prev_node
            
            if self.limitless_mode:
                if self.direction == 'left':
                    last_node.position_x -= self.size
                    if last_node.position_x <= -8:
                        last_node.position_x = 640
                elif self.direction == 'right':
                    last_node.position_x += self.size
                    if last_node.position_x >= 648:
                        last_node.position_x = 0
                elif self.direction == 'up':
                    last_node.position_y -= self.size
                    if last_node.position_y <= -8:
                        last_node.position_y = 544
                elif self.direction == 'down':            
                    last_node.position_y += self.size
                    if last_node.position_y >= 560:
                        last_node.position_y = 0
            
            else:
                if self.direction == 'left':
                    last_node.position_x -= self.size
                    if last_node.position_x <= -8:
                        self.life = 'dead'
                elif self.direction == 'right':
                    last_node.position_x += self.size
                    if last_node.position_x >= 648:
                        self.life = 'dead'
                elif self.direction == 'up':
                    last_node.position_y -= self.size
                    if last_node.position_y <= -8:
                        self.life = 'dead'
                elif self.direction == 'down':            
                    last_node.position_y += self.size
                    if last_node.position_y >= 560:
                        self.life = 'dead'  
    
#----------------------------------------------------------------------------


class Fruit:
    def __init__(self, screen):
        self.screen = screen
        self.color = RED
        self.size = 16
        self.position_x = START_POSITION_FRUIT[0]
        self.position_y = START_POSITION_FRUIT[1]

        self.target_position_x = IMAGINARY_POSITION         # This means that actually there is no target position as it doen't move, but this can change
        self.target_position_y = IMAGINARY_POSITION
        
        self.boost = False      # After eating ceratin fruitsthe player could get a boost on a certain ability 
        self.ninja_mode = False    # Changes target position and it moves towards it, making it harder for the player
        self.speed = 0

        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.position_x + 8, self.position_y + 8), 8)
        
    def move(self):
        self.position_x = random.randint(1,39)*16
        self.position_y = random.randint(1,34)*16
    
    
#-------------------------------------------------------------------------    
    
class Game:
    
    def __init__(self):

        pygame.init() #turn all of pygame on.
        pygame.mixer.init()
        
        self.surface = pygame.display.set_mode(SURFACE)
        pygame.display.set_caption('Snake Game')
        
        self.logo1 = pygame.image.load(os.path.join('Snake_Game_Source_Code/Imagenes', 'logoserp.png'))
        self.gameOver = pygame.image.load(os.path.join('Snake_Game_Source_Code/Imagenes', 'gameoverchi.png'))
        self.explosion = pygame.image.load(os.path.join('Snake_Game_Source_Code/Imagenes', 'explosiongrand.png'))
        
        #self.colision_sound = pygame.mixer.Sound(os.path.join('Snake_Game_Source_Code/Audio', 'colision.wav'))     #TODO
        #pygame.mixer.music.load('Snake_Game_Source_Code/eatfruit.ogg')
        #pygame.mixer.music.play(3)
        #self.eat_sound = pygame.mixer.Sound(os.path.join('Snake_Game_Source_Code/Audio', 'eatfruit.wav'))
        
        self.basic_font = pygame.font.Font(None, 25)
        self.snake = Snake(self.surface, .1)
        self.fruit = Fruit(self.surface)
        self.main_menu = Menu(self.surface, self.basic_font)
        self.pause_menu = PauseMenu(self.surface, self.basic_font)

        self.score = INITIAL_SCORE
        self.multiplier = 0
        self.speed_multiplier = 10
        self.fps = 60
        self.game_state = 'start'
        
        
    def statistics(self):
        pygame.draw.rect(self.surface, WHITE, (0,560,640,90))
        score_msj = self.basic_font.render("SCORE: " + str(int(self.score)), True, (BLACK))
        self.surface.blit(score_msj, (20, 600))
        
        self.surface.blit(self.logo1, (70,295))
        
    def setSpeed(self):
        self.speed_multiplier += 0.2
        self.snake.movement_speed = 1 / self.speed_multiplier   
        
    def update(self):
        self.surface.fill(BLACK)
        self.statistics()
        self.snake.move()
        
        self.fruit.draw()
        self.snake.draw()
        pygame.display.flip()
        time.sleep(self.snake.movement_speed)
        
        self.snake.detectCollision()
        
        
        if self.snake.life == 'dead':
            
            self.surface.fill(BLACK)
            self.snake.draw()
            self.surface.blit(self.explosion, (self.snake.snake_body.snake_head.position_x - 295, self.snake.snake_body.snake_head.position_y - 290))
            pygame.display.flip()
            time.sleep(1)
            
            self.surface.fill(BLACK)    
            time.sleep(1.5)
            self.surface.blit(self.gameOver, (-120, -200))
            pygame.display.flip()
            time.sleep(2)
            
            
            
            if printHighScores(self.surface, self.score) == EXIT_GAME_VALUE:
                return EXIT_GAME_VALUE
        
            chosen_option = self.pause_menu.restartGame()
            
            if chosen_option == EXIT_GAME_VALUE:
                return EXIT_GAME_VALUE
            elif chosen_option == EXIT_TO_MENU_VALUE:
                return EXIT_TO_MENU_VALUE
        
        if self.snake.eatFruit(self.fruit):
            #self.eat_sound.play()      #TODO
            self.fruit.move()
            self.snake.snake_body.add(self.snake)
            self.score += 100 + 100*self.multiplier
            self.multiplier +=.1
            self.setSpeed()    
        
        return CONTINUE_VALUE
    
    def run(self):
        
        menu_selection = self.main_menu.mainMenu()
        
        if menu_selection == EXIT_GAME_VALUE:
            return EXIT_GAME_VALUE    
        
        if self.main_menu.gameModes.endless:
            self.snake.endless_mode = True
        
        if self.main_menu.gameModes.limitless:
            self.snake.limitless_mode = True
        
        self.snake.draw()
        
        pygame.display.flip()
        
        clock = pygame.time.Clock()
        
        while self.game_state != 'end' and self.game_state != 'restart':
            
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state = 'end'
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_state = 'pause'
                    
                    if event.key == K_SPACE:
                        self.snake.snake_color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
                    
                    if (event.key == K_LEFT or event.key == K_a) and self.snake.direction != 'right':
                        self.snake.direction = 'left'
                    
                    if (event.key == K_RIGHT or event.key == K_d) and self.snake.direction != 'left':
                        self.snake.direction = 'right'
                    
                    if (event.key == K_DOWN or event.key == K_s) and self.snake.direction != 'up':
                        self.snake.direction = 'down'
                    
                    if (event.key == K_UP or event.key == K_w) and self.snake.direction != 'down':
                        self.snake.direction = 'up'
            
            if self.game_state == 'pause':
                chosen_option = self.pause_menu.pause()
                if chosen_option == EXIT_GAME_VALUE:
                    self.game_state = 'end'
                elif chosen_option == EXIT_TO_MENU_VALUE:
                    self.game_state = 'restart'
                    #self.pause_menu.restartMenuValues()         # Restarts menu values for next time
                
                else:       # pressed continue
                    self.game_state = 'playing'
                    self.snake.direction = None
                    self.pause_menu.restartMenuValues()         # Restarts menu values for next time
                
            if self.game_state != 'end' and self.game_state != 'restart':
                update_data = self.update()
                if update_data == EXIT_TO_MENU_VALUE:
                    self.game_state = 'restart'
                
                elif update_data == EXIT_GAME_VALUE:
                    self.game_state = 'end'
        
        if self.game_state == 'end':
            del self.snake
            del self.main_menu
            del self.pause_menu
                
            return EXIT_GAME_VALUE
        
        else:       # self.game_state == 'restart'
            del self.snake
            del self.main_menu
            del self.pause_menu
            return EXIT_TO_MENU_VALUE