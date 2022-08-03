from game import *


if __name__ == '__main__':
    
    open('Highscores.txt', 'a+')        # If the file doesn´t exist, it creates it. If it exists, then it doesn't affect the content
    state = True

    snake_game = Game()

    while state:
    
        run = snake_game.run()
    
        if run == EXIT_GAME_VALUE:
            state = False
            del snake_game
    
        elif run == EXIT_TO_MENU_VALUE:
            del snake_game
            snake_game = Game()


    pygame.quit()
    

    