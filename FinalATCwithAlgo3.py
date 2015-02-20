import pygame, sys, time, math, random
from pygame.locals import*
import pdb
import thread,threading
import sys

#import colorama
#from colorama import *
pygame.init()

window = pygame.display.set_mode((700,600))
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKYBLUE = (0, 255, 255)
LIGHTGREEN = (178, 255, 102)
LIGHTPINK = (255, 102, 178)
window.fill(WHITE)

planeList = []  # list containing position of planes
plist = []  # list containing if plane in or out
tlist = [] #list containing tim stamps
alist = [] #stores the angle of orientation
clist = [RED, GREEN, BLUE, SKYBLUE, LIGHTGREEN, LIGHTPINK] 
timegap = [0]

def fangle(f):
    xc = 350
    yc = 300
    slopeNum = float(f[0] - yc)
    slopeDen = float(f[1] - xc)
    slope = slopeNum/slopeDen
    #linXco = slopeNum
    #linYco = -slopeDen
    #slope = linYco/linXco
    if ((f[0] > 350) and (f[1] > 300)):
        angle = math.atan(slope)
    if ((f[0] < 350) and (f[1] > 300)):
        angle = math.pi+math.atan(slope)
    if ((f[0] > 350) and (f[1] < 300)):
        angle = math.atan(slope)
    if ((f[0] < 350) and (f[1] < 300)):
        angle = math.pi+math.atan(slope)
    alist.append(angle)
    
def drawBigc():
    pygame.draw.circle(window, BLUE, (350,300), 150, 1)
    pygame.draw.rect(window, BLACK, (348, 291, 4, 30), 0)
    pygame.display.update()


drawBigc()
pygame.display.update()

def planeMove():
    drawBigc()
    x2 = 500.0
    y2 = 300.0 # x > 350 y < 300
    angle = 0.0
    pygame.draw.circle(window, RED, (int(x2), int(y2)), 10)
    
    
    while(x2 != 350.0 and y2 != 150.0):
        time.sleep(0.05)
        window.fill((255, 255, 255))
        x2 = 350 + 150*math.cos(angle)
        y2 = 300 + 150*math.sin(angle)
        
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
                y2 += 1
            sys.exit()
    
# while(x2 >= 350.0 and y2 >= 300.0) or (x2 <= 350.0 and y2 >= 300.0) or (x2 <= 350.0 and y2 <= 300.0):
# if((int(y2) >= 148 and int(y2) <= 152) and (int(x2) >= 348 and int(x2) <= 355)):

def landPlane(x2, y2):
    while(y2 >= 300):
        pygame.draw.circle(window, RED, (int(x2), int(y2)), 10)
        pygame.display.update()
        y2 += 1

p = 0
i = 0
def planeMove1(aa,ab):
    if(len(planeList) == 0):
        
        drawBigc()
        
    else:
        global i
        i += 1
        xi=planeList[-1][0]
        yi=planeList[-1][1]
        xc=350
        yc=300
        slopeNum = float(yc - yi)
        slopeDen = float(xc - xi)
        slope = slopeNum/slopeDen
        linXco = slopeNum
        linYco = -slopeDen
        cons = -yi*slopeDen + xi*slopeNum
        
        x2 = xc + 150*math.cos(math.atan(slope))
        y2 = yc + 150*math.sin(math.atan(slope))
        c = 0
        pltimjoin = time.localtime(time.time())
        print "Plane ",i," has communicated and is joining the circle at ",x2," ",y2,"at ",str(pltimjoin[3]).zfill(2),":",str(pltimjoin[4]).zfill(2),":",str(pltimjoin[5]).zfill(2),"!!!!"
        
        while (((int(math.sqrt(((xi-350)**2)+((yi-300)**2)))) > 150)):
            l = len(planeList)
            for j in range(0,l):
                if plist[j] == 0:
                    dist = math.sqrt(((planeList[j][0]-planeList[l-1][0])**2)+((planeList[j][1]-planeList[l-1][1])**2))
                    if dist < 10:
                        c = c+0.01
                        continue
                else:
                    dist = math.sqrt(((planeList[j][0]-planeList[l-1][0])**2)+((planeList[j][1]-planeList[l-1][1])**2))-150
                    t=dist/(30*math.pi)
                    x2 = 350 + 150*math.cos(alist[j])
                    y2 = 300 + 150*math.sin(alist[j])
                    x2 = 350 + t*(150*math.cos(alist[j]))
                    y2 = 300 + t*(150*math.sin(alist[j]))
                    
                    x3 = 350 + 150*math.cos(alist[l-1])
                    y3 = 300 + 150*math.sin(alist[l-1])
                    dist = math.sqrt(((x2-x3)**2)+((y2-y3)**2))
                    if dist < 94:
                        c=c+0.01
             
            r = random.randint(0, len(clist) - 1)           
            drawBigc()
            pygame.draw.circle(window, clist[r], (int(xi), int(yi)), 10)
            pygame.display.update()
            window.fill(WHITE)
            drawBigc()
            pygame.display.update()
            time.sleep(0.000005)
            if yi>300:
                yi = yi-1-c
                xi = (cons - linYco*yi)/linXco
            if yi<300:
                yi=yi+1+c
                xi=(cons-linYco*yi)/linXco
            if ((yi==300) and (xi<350)):
                xi=xi+1-c
            if ((yi==300) and (xi>350)):
                xi=xi-1+c
            
            if ((xi>350) and (yi >300)):
                angle = math.atan(slope)
            if ((xi<350) and (yi >300)):
                angle = math.pi+math.atan(slope)
            if ((xi>350) and (yi < 300)):
                angle = math.atan(slope)
            if ((xi<350) and (yi <300)):
                angle = math.pi+math.atan(slope)
        k = i
        #ct = 0
        #print "angle = ",angle,"xi = ",xi,"yi = ",yi,"dist = ",math.sqrt(((xi-350)**2)+((yi-300)**2)),"y2 = ",y2
        print "Plane ",k," has joined the circle at ",x2," ",y2
        while((float(math.sqrt(((xi-350)**2)+((yi-300)**2))-150)< 1.0) and ((int(y2)>=151) or (int(y2)<=149)) or (int(x2) <= 349) or (int(x2) >= 351)):
            #print "angle from while 2 = ",angle    
            window.fill((255, 255, 255))
            x2 = 350 + 150*math.cos(angle)
            y2 = 300 + 150*math.sin(angle)
            time.sleep(0.05)
            drawBigc()
                
            pygame.draw.circle(window, clist[r], (int(x2), int(y2)), 10)
            pygame.display.update()
                
            angle = angle + math.pi/1000
                #print  ((int(x2) >= 349) and (int(x2) <= 351)) and ((int(y2)<151) and (int(y2)>149))
            cont = ((int(x2) >= 349) and (int(x2) <= 351)) and ((int(y2)<=151) and (int(y2)>=149))
            #print "cont = ",cont,"y2 = ",y2,"x2 = ",x2
            #print "while condition = ",(float(math.sqrt(((xi-350)**2)+((yi-300)**2))-150)< 1.0) and ((int(y2)>=151) or (int(y2)<=149) and (int(x2) <= 349) or (int(x2) >= 351))
        cont = ((int(x2) >= 349) and (int(x2) <= 351)) and ((int(y2)<=151) and (int(y2)>=149))
        #print "cont out = ",cont,"y2 out = ",y2,"x2 out = ",x2
        #print "while condition out = ",(float(math.sqrt(((xi-350)**2)+((yi-300)**2))-150)< 1.0) and ((int(y2)>=151) or (int(y2)<=149) and (int(x2) <= 349) or (int(x2) >= 351))
        print "Plane",k," is beginning to land"
        if cont:
            while (int(y2) != 300):
                #ct=ct+1
                window.fill((255, 255, 255))
                drawBigc()
                pygame.draw.circle(window, clist[r], (int(x2), int(y2)), 10)
                pygame.display.update()
                time.sleep(0.05)
                y2 += 1
        global p 
        p += 1
        pltimland = time.localtime(time.time())
        print "Plane ",clist[r]," ",p," has landed at the airport at ",str(pltimland[3]).zfill(2),":",str(pltimland[4]).zfill(2),":",str(pltimland[5]).zfill(2),"!!!!"
        del(tlist[0])
        del(plist[0])
        del(planeList[0])
        

                
def mouseClick(aa,ab):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pltim = time.localtime(time.time())
            timenter = pltim[4]*60+pltim[5]
            timegap.append(timenter)
            print "timegap = ",list(timegap),"condition = ",timegap[-1]-timegap[-2] >= 10
            
            circPos = pygame.mouse.get_pos()
            tlist.append((pltim[3],pltim[4],pltim[5]))
            plist.append(0)
            planeList.append(circPos)
            fangle(circPos)
            
            try:
                thread.start_new_thread(planeMove1,("True",1))
                thread.start_new_thread(mouseClick,("True",1))
            except:
                print "s"
                
            
        
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            continue         
        

while True:
    mouseClick("True",1)


   
            
            
    
