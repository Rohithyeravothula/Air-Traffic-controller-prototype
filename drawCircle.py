import pygame, sys, time, math
from pygame.locals import QUIT

pygame.init()

window = pygame.display.set_mode((700,600))
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
window.fill(WHITE)

def drawBigc():
    pygame.draw.circle(window, BLUE, (350,300), 150, 1)
    pygame.draw.rect(window, BLACK, (348, 291, 4, 30), 0)
    pygame.display.update()

def planeMove():
    drawBigc()
    x2 = 500.0
    y2 = 300.0 # x > 350 y < 300
    angle = 0.0
    pygame.draw.circle(window, RED, (int(x2), int(y2)), 10)
    
    while((x2 != 350.0 and y2 != 150.0)):
        time.sleep(0.05)
        
        x2 = 350 + 150*math.cos(angle)
        y2 = 300 + 150*math.sin(angle)
        window.fill((255, 255, 255))
        drawBigc()
        pygame.draw.circle(window, RED, (int(x2), int(y2)), 10)
        pygame.display.update()
        angle = angle + math.pi/100
     
    time.sleep(0.05)
    if((int(x2) >= 349 and int(x2) <= 351) and int(y2) == 150):
        while(int(y2) != 300):
            window.fill((255, 255, 255))
            drawBigc()
            pygame.draw.circle(window, RED, (int(x2), int(y2)), 10)
            pygame.display.update()
            time.sleep(0.05)
            y2 += 5
    window.fill(WHITE)
    drawBigc()
    pygame.display.update()
    
            
            
    

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            planeMove()
            
            
            
    pygame.display.update()
            
    
