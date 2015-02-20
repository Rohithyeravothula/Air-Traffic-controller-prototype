import pygame,sys
from pygame.locals import*
pygame.init()
white=(255,255,255)
screen=pygame.display.set_mode((500,500))
screen.fill(white)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            pygame.display.update()
            continue
