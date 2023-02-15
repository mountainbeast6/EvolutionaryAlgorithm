import random
import pygame
from player import *
from playerAI import *
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)].x

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item.x < pivot:
            low.append(item)
        elif item.x == pivot:
            same.append(item)
        elif item.x > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)
# start the pygame engine
pygame.init()
camera_pos = (500,500)
circle_off =(500,500)
# start the pygame font engine
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 23)  # load a font for use
gen = 0
# start the sound engine
pygame.mixer.init()

# game variables
simOver = False
camera_offset = (0,0)

map1 = Map(-12)

# game independent variables (needed for every pygame)
FPS = 60  # 60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock()  # used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280, 720))  # initialize the game window
world = pygame.Surface((4000,4000))
best =0
def clear_screen():
    pygame.draw.rect(world, (0, 0, 90), (0, 0, 12000, 12000))

def makeRandomAI():
    players=[]
    for i in range(300):
        players.append(PlayerAI(map1, None))
    return players
players=makeRandomAI()
def breedAI(stupid):
    stupid=quicksort(players)
    print(stupid[0].x)
    print(stupid[299].x)
    for i in range(150):
        stupid.remove(stupid[0])

    for i in range(150):
        where=random.randint(1,200)
        slcob=slice(where)
        slcob2=slice(where, 200)
        which = random.randint(1, 2)
        if which==2:
            stupid.append(PlayerAI(map1,  players[i].dna[slcob]+players[i+1].dna[slcob2]))
            stupid[i+150].randomChange()
        else:
            stupid.append(PlayerAI(map1,  players[i+1].dna[slcob]+players[i].dna[slcob2]))
            stupid[i+150].randomChange()
    for i in range(150):
        stupid[i].reset()
    return stupid
color=(0,0,0)
def draw_mouse_coords(leader):
    textSurface = myfont.render("generation: "+ str(gen)+" best all: "+ str(best)+" best right now: "+str(leader), True, (255,255,255))
    world.blit(textSurface, (50, 70))
def create_map_1():
    map1.add(Platform(400, 530, 30, 400, color))
    map1.add(Platform(400, 940, 400, 30, color))
    map1.add(Platform(480, 670, 400, 30, color))
    map1.add(Platform(900, 870, 400, 30, color))
    map1.add(Platform(1300, 400, 30, 400, color))
    map1.add(Platform(1330, 400, 270, 30, color))
    map1.add(Platform(1800, 200, 800, 30, color))
    map1.add(Platform(2399, 700, 800, 30, color))
    map1.addc(coin(800, 600))
    map1.addc(coin(600, 600))
    map1.addc(coin(800, 900))
    map1.addc(coin(900, 600))
    map1.addc(coin(500, 900))
    map1.addc(coin(875, 900))
    map1.addc(coin(900, 600))
    map1.addc(coin(900, 700))

    map1.addc(coin(1000, 600))
    map1.addc(coin(1100, 400))
    map1.addc(coin(1500, 200))
    map1.addc(coin(400, 400))
    map1.addc(coin(1250, 750))
    map1.addc(coin(1000, 700))
    map1.addc(coin(600, 800))
    map1.addc(coin(1250, 500))
    map1.addc(coin(1350, 350))


    map1.set_gravity(-0.7)

create_map_1()
def update_camera():
    global camera_pos
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        camera_pos = (camera_pos[0]+10, camera_pos[1])
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        camera_pos = (camera_pos[0]-10, camera_pos[1])
    if pygame.key.get_pressed()[pygame.K_UP]:
        camera_pos = (camera_pos[0], camera_pos[1]-10)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        camera_pos = (camera_pos[0], camera_pos[1]+10)

# main while loop
while not simOver:
    # loop through and empty the event queue, key presses
    # buttons, clicks, etc.
    for event in pygame.event.get():

        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            simOver = True
    clear_screen()
    map1.draw(world)
    x_offset = 0
    y_offset = 0
    greatestnum=0
    greatestind=0
    update_camera()
    for i in range(300):
        if len(players[i].coins) >greatestnum:
            greatestind=i
            greatestnum=len(players[i].coins)
    for p in players:
        p.draw(world)
        p.act()
    if players[0].currentAllele==200:
        players=breedAI(players)
        gen+=1
        if best<greatestnum:
            best=greatestnum
    textSurface = myfont.render("generation: "+ str(gen)+" best all: "+ str(round(best))+" best right now: "+str(round(greatestnum)), True, (255,255,255))



    x_offset = 640 - camera_pos[0]
    y_offset = 350 - camera_pos[1]
    camera_offset = (x_offset, y_offset)
    world.blit(textSurface, (50 - x_offset, 300-y_offset))
    cx_offset = players[greatestind].x
    cy_offset = players[greatestind].y
    circle_off = (cx_offset+camera_offset[0]+15, cy_offset+camera_offset[1]+15)
    # put all the graphics on the screen
    screen.blit(world,camera_offset)
    pygame.draw.circle(screen, (0, 0, 0), (circle_off), 15, 3)
    # should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS)  # slow the loop down to 60 loops per second