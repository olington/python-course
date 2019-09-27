# Кондрашова О.
# ИУ7-25

import pygame
import sys
import random
import math
from pygame.locals import *

# Цвета
#                 R    G    B
black =         (  0,   0,   0)
white =         (255, 255, 255)
cosmos =        ( 20,  47,  91)
blue =          (186, 218, 242) 
green =         ( 33, 165,  72) 
grey =          (158, 158, 158)
yellow =        (255, 215,   0)

# Константы
screen_width = 1000
screen_height = 700

# Дисплей
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation")

# Траектория движения НЛО
def f(x): return round(((x*x)/1000) - x) + 400

ufo = {'x': 0}
sput = {'z': 1030}

# Прорисовка НЛО
def ship(x):
    pygame.draw.circle(screen, blue, [x, f(x)], 45)
    pygame.draw.ellipse(screen, green, [(x-90, f(x)), (180, 60)])

# Прорисовка спутника
def sputnik(x):
    pygame.draw.circle(screen, grey, [x, 500], 60)
    pygame.draw.circle(screen, black, [x-30, 480], 20)
    pygame.draw.line(screen, grey, [x, 500], [x+200,430], 15)
    pygame.draw.line(screen, grey, [x, 500], [x+180,500], 15)
    pygame.draw.line(screen, grey, [x, 500], [x+200,570], 15)

# Прорисовка звезд
def stars(size):
    pygame.draw.circle(screen, yellow, [50, 100], size)
    pygame.draw.circle(screen, yellow, [150, 650], size)
    pygame.draw.circle(screen, yellow, [750, 200], size)
    pygame.draw.circle(screen, yellow, [700, 600], size)
    pygame.draw.circle(screen, yellow, [250, 500], size)
    pygame.draw.circle(screen, yellow, [450, 350], size)
    pygame.draw.circle(screen, yellow, [300, 250], size)
    pygame.draw.circle(screen, yellow, [550, 150], size)
    pygame.draw.circle(screen, yellow, [550, 550], size)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill(cosmos)
    rad = random.randint(5, 7)
    stars(rad)
    ship(ufo['x'])
    ufo['x'] += 2
    if ufo['x'] >=1090:
        ufo = {'x': 0}
    sputnik(sput['z'])
    sput['z'] -= 3
    if sput['z'] <= -200:
        sput = {'z': 1030}
    pygame.display.update()
