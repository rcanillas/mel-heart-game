import pygame
import sys
from pygame.locals import *
from random import *

SPEED = 1
TIME = 1
# FPS
FPS = 60
# Window
HEIGHT = 700
WIDTH = 900


def updateMousePosition(posx, posy, catposx, catposy, current_frame):
    speedx = 0
    speedy = 0

    if current_frame % 60 == 0:
        speedx = randint(-15, 15)
        speedy = randint(-15, 15)

    print speedx, speedy

    posx += speedx
    posy += speedy
    if posx < 0:
        posx = 0
    if posy < 0:
        posy = 0
    if posx > WIDTH:
        posx = WIDTH
    if posy > HEIGHT:
        posy = HEIGHT


 #   if (posx == 0) or (posx == WIDTH):
#       posx = posx
#    else:
#        if catposx >= posx:
 #           posx += - speed
 #       if catposx < posx:
 #           posx += speed
#
 #   if (posy == 0) or (posy == HEIGHT):
  #      posy = posy
  #  else:
 #       if catposy >= posy:
 #           posy += - speed
 #       if catposy < posy:
 #           posy += speed
   # print "Goal position : %d %d  Current position : %d %d " % (newposx, newposy, posx, posy)

    return posx, posy


def updateCatPosition(oldposy, oldposx, goalx, goaly, current_frame):
    posx = oldposx
    posy = oldposy
    if current_frame >= TIME*FPS:
        posx = goalx
        posy = goaly
        # print "time up"

    else:
        lenx = goalx - oldposx
        leny = goaly - oldposy
        # print lenx, leny

        speedX = float(lenx) / float(TIME*FPS)
        speedY = float(leny) / float(TIME*FPS)

        # print speedX, speedY
        posx += current_frame*speedX
        posy += current_frame*speedY
        # print posx, posy
        current_frame += 1

    return posx, posy, current_frame


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    pygame.display.set_caption('Cat !')
    fpsClock = pygame.time.Clock()
    # Colors
    TEAL = (0, 128, 128, 255)
    BLUE = (0, 0, 250, 255)
    WHITE = (255, 255, 255, 255)
    NONE = (255, 255, 255, 255)

    # Sounds
    catMeow = pygame.mixer.Sound('CatMeow.ogg')
    # catMeow.play()

    # Texts
    fonObj = pygame.font.Font("freesansbold.ttf", 32)
    textSurfaceObj = fonObj.render('Cat !', True, BLUE, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH / 2, HEIGHT / 2)
    # Images
    catIMG = pygame.image.load('cat_PNG.png')
    catIMG = pygame.transform.scale(catIMG, (150, 100))
    catRect = catIMG.get_rect()

    mouseIMG = pygame.image.load('mouse_PNG.png')
    mouseIMG = pygame.transform.scale(mouseIMG, (50, 50))
    mouseRect = mouseIMG.get_rect()

    smallRect = pygame.Rect(0, HEIGHT / 2, 25, 25)

    # Drawing

    pygame.draw.rect(DISPLAYSURF, TEAL, smallRect)

    mouseX = randint(0, WIDTH)
    mouseY = randint(0, HEIGHT)

    newCatx = catx = tempcatx = catx2 = 50
    newCaty = caty = tempcaty = caty2 = 50
    meow = False
    current_frame = TIME*FPS


    # Game Loop
    while True:

        DISPLAYSURF.fill(WHITE)
        catRect.center = (tempcatx, tempcaty)
        mouseRect.center = (mouseX, mouseY)
        DISPLAYSURF.blit(catIMG, catRect)
        DISPLAYSURF.blit(mouseIMG, mouseRect)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        # DISPLAYSURF = DISPLAYSURF.convert_alpha()



        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                (newCatx, newCaty) = event.pos
                (caty, catx) = catRect.center
                current_frame = 1
                meow = True

        # catx, caty = updatedposition(catx, caty, newCatx, newCaty)
        tempcatx, tempcaty, current_frame = updateCatPosition(catx, caty, newCatx, newCaty, current_frame)

        (mouseX, mouseY) = updateMousePosition(mouseX, mouseY, tempcatx, tempcaty, current_frame)
        if catRect.colliderect(mouseRect) and meow:
            # print "Meow"
            catMeow.play()
            meow = False
            mouseX = randint(0, WIDTH)
            mouseY = randint(0, HEIGHT)



        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
