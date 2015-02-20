import wx
import threading
import numpy as np
import time
import pygame,sys
from pygame.locals import *
from math import *


zeropoint=0
pl=[]
cl=[]
cl.append(str(500))
x10=0
y10=0
tspeed=0
crrnt=[0 for i in range(0,24)]
fcrrnt=[0 for i in range(0,24)]
###############################################################################
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            
            #print"busy"
            self.event.wait(p)

    def stop(self):
        self.event.set()



###############################################################################
def sector(x,y):
    ang=np.arctan(abs(y-300)/abs(x-300))
    div=(2*3.14)/24
    if x>300 and y<300:
        angle=(3.14/2)-ang
    if x>300 and y>300:
        angle=(3.14/2)+ang
    if x<300 and y<300:
        angle=(3*3.14/2)+ang
    if x<300 and y>300:
        angle=(3*3.14/2)-ang
    return int(angle/div)
    

###############################################################################

###############################################################################        

################################################################################
def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3BUTTON1, wxID_FRAME3PANEL1, wxID_FRAME3STATICTEXT1, 
 wxID_FRAME3STATICTEXT2, wxID_FRAME3STATICTEXT3, wxID_FRAME3STATICTEXT4, 
 wxID_FRAME3TEXTCTRL1, wxID_FRAME3TEXTCTRL2, wxID_FRAME3TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(605, 148), size=wx.Size(484, 177),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Airplane Controls')
        self.SetClientSize(wx.Size(468, 139))
        self.SetBackgroundColour(wx.Colour(168, 168, 168))

        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(468, 139),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
              label=u'X Coordinate  '+str(x10-300), name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 24), size=wx.Size(74, 16), style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        

       

        self.staticText3 = wx.StaticText(id=wxID_FRAME3STATICTEXT3,
              label=u'Y Coordinate  '+str(300-y10), name='staticText3', parent=self.panel1,
              pos=wx.Point(240, 24), size=wx.Size(74, 16), style=0)
        self.staticText3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        

        self.staticText4 = wx.StaticText(id=wxID_FRAME3STATICTEXT4,
              label=u'Speed', name='staticText4', parent=self.panel1,
              pos=wx.Point(152, 56), size=wx.Size(36, 16), style=0)
        self.staticText4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME3TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(208, 56), size=wx.Size(96, 16),
              style=0, value=u'')
        self.textCtrl3.Bind(wx.EVT_TEXT, self.OnTextCtrl3Text,
              id=wxID_FRAME3TEXTCTRL3)

        self.button1 = wx.Button(id=wxID_FRAME3BUTTON1, label=u'OK',
              name='button1', parent=self.panel1, pos=wx.Point(184, 96),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME3BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTextCtrl3Text(self, event):
        cl.append(self.textCtrl3.GetValue())

    def OnButton1Button(self, event):
        self.Close(1)

    


    
    



################################################################################

###############################################################################
#code for running on runway begins.....

def runway(a1,b1,f,c):
    f=1
    sec1 = sector(a1+300,-b1+300)
    if (a1 > 0 and a1<10 and b1 >172 and b1 < 178):
        crrnt[int(sec1)]=0
        crrnt[int(sec1+1)%24]=0
        crrnt[int(sec1+2)%24]=0
        crrnt[int(sec1-1)%24]=0
        crrnt[int(sec1-2)%24]=0
        l=122
        
        while l<300:
            
            pl[c]=[300,l]
            l += 3
            
            time.sleep(0.1)
        f=0
    return f    
        
#code for running on runway ends..........

#############################################################################


################################################################################################################
#for rotating in circle code begins......


def circle(x1,y1,c):
    if x1<300 :
        
        theta=np.arctan((300-y1)/(x1-300))
    
        for i in np.arange(theta+3.14,100,0.05):
        
            a=177*(np.cos(i))
            b=177*(np.sin(i))
            f=1
            if runway(a,b,f,c)==0:
                #print crrnt
                break
            pl[c]=[a+300,-b+300]

            sec1=(sector(a+300,-b+300))
            
            if int(sec1)!=0:                   
                crrnt = [0 for i in range (0,24)]
                crrnt[int(sec1)]=1
                crrnt[int(sec1+1)%24]=1
                crrnt[int(sec1+2)%24]=1
                crrnt[int(sec1-1)%24]=1
                crrnt[int(sec1-2)%24]=1
                crrnt[int(sec1+3)%24]=0
                #print crrnt,sec1
            time.sleep(0.1)
           
   
    if x1>300 :
        theta=np.arctan((300-y1)/(x1-300))        
        for i in np.arange(theta,100,0.05):
            
            a=177*(np.cos(i))
            b=177*(np.sin(i))
            f=1
            if runway(a,b,f,c)==0:
                crrnt=[0 for i in range(0,24)]
                #print crrnt
                break
            
            
            pl[c]=[a+300,-b+300]
            sec1=sector(a+300,-b+300)
            if sec1==0:
                crrnt[int(sec1)]=0
                crrnt[int(sec1+1)%24]=0
                crrnt[int(sec1+2)%24]=0
                crrnt[int(sec1-1)%24]=0
                crrnt[int(sec1-2)%24]=0
                
            else:
                crrnt = [0 for i in range (0,24)]
                crrnt[int(sec1)]=1
                crrnt[int(sec1+1)%24]=1
                crrnt[int(sec1+2)%24]=1
                crrnt[int(sec1-1)%24]=1
                crrnt[int(sec1-2)%24]=1
               # crrnt[int(sec1+3)%24]=0
               # print crrnt,sec1  
            time.sleep(0.1)
           
    
#for rotating in circle code ends.....    

#################################################################################
        
################################################################################    

#main begins.....



pygame.init()
screen=pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("Air Traffic Control (ATC)")
background=pygame.image.load("bg.jpg").convert()
plane=pygame.image.load("plane.png").convert_alpha()
screen.blit(background,(7,7))
pygame.display.update()




################################################################################

################################################################################
# code for coming to the circle begins here......called by     ""thread""

def move(x,y,c):


    pl.append([x,y])
    
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()
 
    app.MainLoop()
    
    t=new_plane(x,y)

    if t<24 and len(pl)!=1:
           
        tmr = TimerClass()
        tmr.start()
        l=(t-sector(x,y))*2*3.14*187.5/24
        d=sqrt((x-300)**2 + (y-300)**2)-187.5
        tim=(l-d)*0.1/(187.5*0.05)
        
        p=abs(1)
        time.sleep(p)
        tmr.stop()
    if cl[len(cl)-1]=='':
        cl[len(c1)-1]=500
    tspeed = (500*0.1)/(int(cl[len(cl)-1])) 
    thet=np.arctan(abs(y-300)/abs(x-300))

    if(x>300 and y<300):
        
        while(sqrt((x-300)**2 + (y-300)**2)>180):
           
            
            x -= 5*np.cos(thet)
            y += 5*np.sin(thet)
            pl[c]=[x,y]
            
            time.sleep(tspeed)
            

    if(x>300 and y>300):
        thet=np.arctan(abs(y-300)/abs(x-300))
        while(sqrt((x-300)**2 + (y-300)**2)>180):
          
           
            x -= 5*np.cos(thet)
            y -= 5*np.sin(thet)
            pl[c]=[x,y]
            
            time.sleep(tspeed)


    if(x<300 and y<300):
        while(sqrt((x-300)**2 + (y-300)**2)>180):
        
            
            x += 5*np.cos(thet)
            y += 5*np.sin(thet)
            pl[c]=[x,y]
            
            time.sleep(tspeed)  



    if(x<300 and y>300):
        while(sqrt((x-300)**2 + (y-300)**2)>180):
           
            
            x += 5*np.cos(thet)
            y -= 5*np.sin(thet)
            pl[c]=[x,y]
           
            time.sleep(tspeed)
    
    

    
   

    
    circle(x,y,c)
    
    

#code for coming to the circle ends here.....

###############################################################################
def new_plane(x,y):
    future(x,y)
    sec=sector(x,y)
    zeropoint=-2
    if crrnt[int(sec)]==0:
       zeropoint=-1
       crrnt[int(sec)]=1
       crrnt[int(sec+1)%24]=1
       crrnt[int(sec+2)%24]=1
       crrnt[int(sec-1)%24]=1
       crrnt[int(sec-2)%24]=1
    
    else:
        x=int(sec)
        count=0
        while count<24:
            if crrnt[x]==0:
                zeropoint=x
                break
            x=(x+1)%24
            count+=1
    return zeropoint

                
###############################################################################
def future(x,y):
    fcrrnttemp=[0 for i in range(0,24)]
    d=sqrt((x-300)**2 + (y-300)**2)-187.5
    T=d*tspeed/(187.5*0.05)
    for i in range(0,24):
        fcrrnt[i%24]=crrnt[i%24]
        fcrrnttemp[i%24]=crrnt[i%24]
    t=0.1*2*3.14/(24*187.5*0.05)
    steps=int(T/t)
   
        
    while steps>0:
        for i in range(0,24):
            fcrrnt[(i-1)%24]=fcrrnttemp[i%24]
        for i in range(0,24):
            fcrrnttemp[i%24]=fcrrnt[i%24]
        steps-=1    
            
    
################################################################################
c=0
p=0
while True:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            x=x-12.5
            y=y-12.5
            c=c+1
            x10=x
            y10=y
            threading.Thread(target=move,args=(x,y,c-1)).start()
            
                
    screen.blit(background,(7,7))
    for i in range(0,len(pl)):
        
        screen.blit(plane,(pl[i][0],pl[i][1]))
    pygame.display.update()
        
            
                

#    main ends.....
###############################################################################
