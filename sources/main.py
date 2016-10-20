import pygame
import sys
from pygame.locals import *

SPEED = 5
# FPS
FPS = 60
# Window
HEIGHT = 500
WIDTH = 500


def updatedposition(posx, posy, newposx, newposy):
    if (newposx - posx) >= 5:
        posx += SPEED
    else:
        posx = posx

    if (newposx - posx) <= 5:
        posx -= SPEED
    else:
        posx = posx

    if (newposy - posy) >= 5:
        posy += SPEED
    else:
        posy = posy

    if (newposy - posy) <= 5:
        posy -= SPEED
    else:
        posy = posy
    #print "Goal position : %d %d  Current position : %d %d " % (newposx, newposy, posx, posy)

    return posx, posy


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    # DISPLAYSURF = DISPLAYSURF.convert_alpha()
    pygame.display.set_caption('Cat !')
    fpsClock = pygame.time.Clock()
    # Colors
    TEAL = (0, 128, 128)
    BLUE = (0, 0, 250)
    WHITE = (255, 255, 255)

    # Sounds
    catMeow = pygame.mixer.Sound('CatMeow.ogg')
    catMeow.play()

    # Texts
    fonObj = pygame.font.Font("freesansbold.ttf", 32)
    textSurfaceObj = fonObj.render('Cat !', True, BLUE, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH / 2, HEIGHT / 2)
    # Images
    catIMG = pygame.image.load('cat_PNG.png')
    catIMG = pygame.transform.scale(catIMG, (150, 100))
    catRect = catIMG.get_rect()
    smallRect = pygame.Rect(0, HEIGHT / 2, 25, 25)

    # Drawing

    pygame.draw.rect(DISPLAYSURF, TEAL, smallRect)

    newCatx = catx = 50
    newCaty = caty = 50
    meow = False
    # Game Loop
    while True:


        DISPLAYSURF.fill(WHITE)
        catRect.center=(catx, caty)
        DISPLAYSURF.blit(catIMG, catRect)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                (newCatx, newCaty) = event.pos
                meow = True

        catx, caty = updatedposition(catx, caty, newCatx, newCaty)
        if (abs(newCatx - catx) <= 10) and (abs(newCaty - caty) <= 10) and meow:
            print "Meow"
            catMeow.play()
            meow = False

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
