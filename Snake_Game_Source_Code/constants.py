import pygame
import time
import random
import os

from pygame.locals import *

# CONSTANTS

SURFACE = (640, 650)

START_POSITION_PLAYER = (80, 80)
START_POSITION_FRUIT = (160, 160)

INITIAL_SCORE = 0

EXIT_GAME_VALUE = -1
EXIT_TO_MENU_VALUE = -2
CONTINUE_VALUE = 1

#-------------------------
#       COLORS
#-------------------------


LIGHT_BLUE = (0,247,250)
GREEN = (60,220,60)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
GREY = (150,150,150)
YELLOW = (249,215,28)
ORANGE = (255, 191, 0)