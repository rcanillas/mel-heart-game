import pygame
import sys
from pygame.locals import *

pygame.init()
#FPS
FPS = 60
fpsClock = pygame.time.Clock()

# Window
HEIGHT = 400
WIDTH = 500
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
# DISPLAYSURF = DISPLAYSURF.convert_alpha()
pygame.display.set_caption('Drawing')

# Colors
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)

# Images
catIMG = pygame.image.load('cat_PNG.png')
catIMG = pygame.transform.scale(catIMG, (50, 75))
catx = 10
caty = 10
direction = 'right'
smallRect = pygame.Rect(WIDTH/2, HEIGHT/2, 25, 25)

# Drawing

pygame.draw.rect(DISPLAYSURF, TEAL, smallRect)


# Game Loop
while True:
    DISPLAYSURF.fill(WHITE)

    # Image position update
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catIMG, (catx, caty))
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
