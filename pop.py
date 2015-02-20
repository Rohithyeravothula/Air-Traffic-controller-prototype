import pygame
from pygame.locals import*
import time,math
def main():
    pygame.init()
    window=pygame.display.set_mode((500,500))
    window.fill((255,255,255))
    pygame.display.update()
    txtbz=eztext.Input(maxlenth=10, color=(0,0,0),prompt='give')
    while 1:
        for evnt in pygame.event.get():
            if event.type == QUIT:
                screen.fill((255,255,255))
                txtbx.update(pygame.events.get())
                txtbx.draw(screen)
                pygame.display.flip()
if __name__ == '__main__':main()
