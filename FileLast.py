import thread
import time
import pygame,sys,pdb
from pygame.locals import *
import math

pygame.init()
pywindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Draw Circle at Cursor!')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
pywindow.fill(WHITE)
pygame.display.update()
circlInfo = []
pointslist = []

def drawCirc(st,rad):
    pygame.draw.circle(pywindow, BLUE, (200,200), rad, 1)
    pygame.display.update()
        
def move(st,a):
    
            
def cir(st,l):
    print "hi"
    while True: #main game loop
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    circ = pygame.mouse.get_pos()
                    pointslist.append(circ)
                    print circ
                    pygame.draw.circle(pywindow, BLUE, (circ), 10)
                    pygame.display.update()
                if event.type == QUIT:
                    
                    pygame.quit()
                    sys.exit()
                
try:
    thread.start_new_thread(move,("True",0.05))
    thread.start_new_thread(cir("True",1))
except:
    print "unable"
    






