import pygame,pdb
import math
import time
import thread,threading
from pygame.locals import*

pygame.init()
window=pygame.display.set_mode((500,500))

white = (255,255,255)
black = (0,0,0)

window.fill(white)
pygame.display.update()

a=[[100,100],[300,100]]
def drw():
    l=len(a)
    for i in range(0,l):
        pygame.draw.circle(window,black,(a[i][0],a[i][1]),3,0)
        
    pygame.display.update()
    time.sleep(0.05)
    for i in range(0,l):
        pygame.draw.circle(window,white,(a[i][0],a[i][1]),3,0)

for j in range(0,100):
    a[0][0]=a[0][0]+1
    a[1][0]=a[1][0]+1
    drw()
        


    
    
    
     
