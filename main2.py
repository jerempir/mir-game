import pygame
import random
from copy import deepcopy


def glider1(current_field,x,y):
    pos = [(x,y),(x+1,y+1),(x-1,y+2),(x,y + 2),(x+1,y+2)]
    for i,j in pos:
        current_field[j][i] = 1
    return current_field

def glider2(current_field,x,y):
    pos = [(x,y),(x-2,y-1),(x-2,y),(x-2,y +1),(x-1,y-1)]
    for i,j in pos:
        current_field[j][i] = 1
    return current_field

def glidermake(current_field):
    for k in range(20):
        i0,j0 = random.randrange(cellsize,W//2 + W//4,cellsize), random.randrange(cellsize,H//2)
        current_filed = glider1(current_field,i0,j0)
        i1, j1 = random.randrange(W // 2 - W // 4,W - cellsize), random.randrange( H // 2,H-cellsize)
        current_filed = glider2(current_filed,i1,j1)
    return current_field

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

def erase(mass):
    mass = [[0 for i in range(W)] for j in range(H)]
    return mass

RES = WIDTH, HEIGHT = 1200, 700
cellsize= 20
W, H = WIDTH// cellsize, HEIGHT//cellsize
FPS = 20
stop = False
next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[0 for i in range(W)] for j in range(H)]

#start1 = glidermake(current_field)
start2 = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
start3 = [[random.randint(0, 1) for i in range(W)] for j in range(H)]
start4 = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)] # 2,5,8,9,10,11,13,18,21,22,26,30,33,65
start5 = [[1 if not (2 * i + j) % 4 else 0 for i in range(W)] for j in range(H)] # (2,4),(4,4)
start6 = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
start7 = [[1 if not i % 7 else random.randint(0, 1) for i in range(W)] for j in range(H)]

current_field = start7
pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    surface.fill(pygame.Color('black'))
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, cellsize)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, cellsize)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            x,y = pygame.mouse.get_pos()
            x = x // cellsize
            y = y // cellsize
            print(y, x)
            current_field[y][x] =1 #not current_field[y][x]
        if pressed[2]:stop = not stop
        if pressed[1]: current_field = erase(current_field)
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('green'), (x * cellsize + 2, y * cellsize + 2, cellsize - 2, cellsize - 2))
            if stop == False:
                next_field[y][x] = check_cell(current_field, x, y)
    if stop == False:
        current_field = deepcopy(next_field)
   #print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)