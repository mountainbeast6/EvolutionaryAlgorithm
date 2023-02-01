import random
import pygame
from player import *

# start the pygame engine
pygame.init()

# start the pygame font engine
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 23)  # load a font for use

# start the sound engine
pygame.mixer.init()

# game variables
simOver = False

map1 = Map(-12)
p1 = Player(map1)
# game independent variables (needed for every pygame)
FPS = 60  # 60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock()  # used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280, 720))  # initialize the game window


def clear_screen():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 720))


def create_map_1():
    map1.add(Platform(100, 500, 400, 30, (145, 105, 200)))
    map1.add(Platform(600, 600, 100, 30, (145, 105, 200)))
    map1.set_gravity(-0.3)


create_map_1()
p1.set_map(map1)

# main while loop
while not simOver:
    # loop through and empty the event queue, key presses
    # buttons, clicks, etc.
    for event in pygame.event.get():

        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            simOver = True
    clear_screen()
    p1.draw(screen)
    map1.draw(screen)
    p1.act()
    # put all the graphics on the screen
    # should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS)  # slow the loop down to 60 loops per second
