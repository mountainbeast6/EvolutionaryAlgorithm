import random
import pygame
from player import *
from playerAI import *

# start the pygame engine
pygame.init()

# start the pygame font engine
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 23)  # load a font for use

# start the sound engine
pygame.mixer.init()

# game variables
simOver = False
camera_offset = (0,0)

map1 = Map(-12)
p1 = PlayerAI(map1)
# game independent variables (needed for every pygame)
FPS = 60  # 60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock()  # used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280, 720))  # initialize the game window
world = pygame.Surface((3000,3000))

def clear_screen():
    pygame.draw.rect(world, (0, 0, 0), (0, 0, 3000, 3000))


def create_map_1():
    map1.add(Platform(400, 530, 30, 400, (145, 105, 200)))
    map1.add(Platform(400, 940, 400, 30, (145, 105, 200)))
    map1.add(Platform(480, 670, 400, 30, (145, 105, 200)))
    map1.add(Platform(900, 870, 400, 30, (145, 105, 200)))
    map1.addc(coin(200, 500))

    map1.set_gravity(-0.7)


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
    p1.draw(world)
    map1.draw(world)
    p1.act()
    player_pos = p1.act()
    p1.act()
    x_offset = 0
    y_offset = 0
    x_offset = 640 - player_pos[0]
    y_offset = 350 - player_pos[1]
    camera_offset = (x_offset, y_offset)
    # put all the graphics on the screen
    screen.blit(world,camera_offset)
    # should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS)  # slow the loop down to 60 loops per second
