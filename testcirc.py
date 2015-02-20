from array import*
import pygame, sys
import math
import time
timec=time.localtime(time.time())  # program start time 
a=array('i',[]) #array of angles of planes in C.path
b=array('L',[])  #array of new planes
from pygame.locals import *

def calangle(n):
    r= math.atan((math.fabs(n[1]-500))/math.fabs((n[0]-500)))*(180/math.pi)
    if ((n[1]-500)<0 and (n[0]-500)<0):
        return 180.0-r
    if ((n[1]-500)>0 and (n[0]-500)<0):
        return 180.0+r
    if ((n[1]-500)>0 and (n[0]-500)>0):
        return 270.0+r
    if ((n[1]-500)<0 and (n[0]-500)>0):
        return r
                             
    
    
#drawing circles

class Particle:
    def __init__(self, (x, y), size, colour):
        self.x = x
        self.y = y
        self.size = size
        #self.colour = (0, 0, 255)
        self.colour = colour
        self.thickness = 1
    def display(self):
        pygame.draw.circle(pywindow, self.colour, (self.x, self.y), self.size, self.thickness)

pygame.init()
pywindow = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption('Draw Circle at Cursor!')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
pywindow.fill(WHITE)

my_first_particle=Particle((500,500),400,(0,0,255))
my_first_particle.display()

while True: #main game loop
    angle = 0.0
    while angle <=2*math.pi:
        time.sleep(0.05)
        pywindow.fill((255, 255, 255))
        x2 = 250 + 100*math.cos(angle)
        y2 = 250 + 100*math.sin(angle)
        my_first_particle = Particle((250, 250), 100, (0, 0, 255))
        my_first_particle.display()
        pygame.draw.circle(pywindow, (255, 0, 0), (int(x2), int(y2)), 10)
        pygame.display.update()
        angle = angle + math.pi/100

    
    for event in pygame.event.get():
        angle = 0.0
        while angle <=2*math.pi:
            time.sleep(0.05)
            pywindow.fill((255, 255, 255))
            x2 = 250 + 100*math.cos(angle)
            y2 = 250 + 100*math.sin(angle)
            my_first_particle = Particle((250, 250), 100, (0, 0, 255))
            my_first_particle.display()
            pygame.draw.circle(pywindow, (255, 0, 0), (int(x2), int(y2)), 10)
            pygame.display.update()
            angle = angle + math.pi/100
        if event.type == pygame.MOUSEBUTTONDOWN: #This checks for the mouse press event
            circ = pygame.mouse.get_pos() #Gets the mouse position
            angle=calangle(circ)
            timep=time.localtime(time.time())   #time at plane input
            print circ,angle,math.fabs(timep[3]-timec[3]),math.fabs(timep[4]-timec[4]),math.fabs(timep[5]-timec[5])
            
            pygame.draw.circle(pywindow, BLUE, (circ), 10) #Draws a circle at the mouse position!
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# put centre of circle at 500,500

