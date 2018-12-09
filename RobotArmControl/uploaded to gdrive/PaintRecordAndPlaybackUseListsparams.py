from pygame import *
import tkinter as tk
import tkinter.messagebox
#from tkinter import *
import pynput
import pygame,sys
import time

#mkeyboard = pynput.keyboard.Controller()

pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([0,0,255])
x=1
#
# #pygame.init()
# root=Tk()
# root.mainloop()

#def replayMoves():
        # get array of positions
        #divide them into coordinates
        #start animation

def tkscreentest():
    finished = False
    rr=255
    gg=255
    bb=255
    screen = pygame.display.set_mode([640,480])
    screen.fill([rr, gg, bb])
    x = 50
    y = 50
    x_speed = 10
    yy=1
    last=1
    operation = "Ready"
    while finished == False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == K_x:
                tt = yy-1
                finished=True
            if event.type == pygame.KEYDOWN and event.key == K_c:
                operation = "Circle"
            if event.type == pygame.KEYDOWN and event.key == K_r:
                operation = "Rectangle"
            if event.type == pygame.KEYDOWN and event.key == K_e:
                operation = "Ellipse"
            if event.type == pygame.KEYDOWN and event.key == K_l:
                operation = "Line"
        yy=yy+1
        #im = pygame.Surface((200, 200))
        pygame.time.delay(20)
        x = x + x_speed
        if x > 480 or x < 0:
            x_speed = -x_speed
        #screen.blit(my_ball, [x, y])
        pygame.display.flip()
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        pygame.draw.rect(screen, [128, 127, 128], [mouseX, mouseY, 50, 50], 1)
        #recordPosition=[mouseX,mouseY]
        #pygame.draw.rect(screen, [128, 255, 128], [240, 360, 50, 50], 0)
        # print(mousedown," --- ")
        # def get_user_input(r, g, b):
        # left = tk.mouse_buttons()
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        button_pressed = pygame.mouse.get_pressed()
        fill = 0
        nofill = 1

        # print (button_pressed,"mmmoouuasee")
        if (button_pressed[0] == True):
            print("Left button pressed")
            rr = 0
            gg = 0
            bb = 255
            pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 80, 0)
            pygame.draw.rect(screen, [0, 0, 255], [mouseX, mouseY, 50, 50], 0)
        else:
            if (button_pressed[1] == True):
                rr = 0
                gg = 255
                bb = 0
                print("Middle button pressed")
                pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 80, 0)
                pygame.draw.rect(screen, [0, 255, 0], [mouseX, mouseY, 50, 50], 0)
            else:
                if (button_pressed[-1] == True):
                    rr = 255
                    gg = 0
                    bb = 0
                    print("Right button pressed")
                    pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 80, 0)
                    pygame.draw.rect(screen, [255, 0, 0], [mouseX, mouseY, 50, 50], 0)
        if (button_pressed[0] == True and button_pressed[-1] == True):
            rr=255
            gg=255
            bb=255
            pygame.draw.rect(screen, [rr, gg, bb], [mouseX, mouseY, 50, 50], 0)
        #
        # if(mouseX >= 80 and mouseX <=100 and mouseY>=400 and mouseY<=420):
        #     #pygame.draw.circle(screen, [0, 255, 0], [180, 400], 40, 0)
        #     pygame.draw.rect(screen, [rr, gg, bb], [240, 360, 50, 50],1 )
        # #screen.fill([255, 0, 255])
        # else:
        #     if (mouseX <= 80 and mouseX >= 100 and mouseY <= 400 and mouseY >= 420):
        #         pygame.draw.rect(screen, [0, 0, 0], [240, 360, 50, 50], 0)
        #pygame.draw.circle(screen, [255, 255, 0], [180, 400], 40, 0)
        #screen.fill([255,255,255])
        separator=" - "
        op.insert(yy,operation)
        recordXpos.insert(yy,mouseX)
        recordSep.insert(yy,separator)
        recordYpos.insert(yy,mouseY)
        r.insert(yy,rr)
        g.insert(yy,gg)
        b.insert(yy,bb)
        #recordPosition = [mouseX, mouseY]
        print(operation,mouseX, mouseY,r,g,b)
        print("")
    tt=yy
    return




def playscreentest():
    screen = pygame.display.set_mode([640,480])
    screen.fill([255, 255, 255])
    #my_ball = pygame.image.load('duke.gif')
    x = 50
    y = 50
    x_speed = 10
    yy=1
    allofit=int(len(recordXpos))
    print("Doing play back")
    for yy in range(allofit):
        #im = pygame.Surface((200, 200))
        pygame.time.delay(20)
        pygame.display.flip()
        mouseXx = recordXpos[yy]
        mouseYy = recordYpos[yy]
        red=r[yy]
        green=g[yy]
        blue=b[yy]
        pygame.draw.rect(screen, [red, green, blue], [mouseXx, mouseYy, 50, 50], 0)
        #pygame.draw.rect(screen, [r[yy], g[yy], b[yy]], [mouseXx, mouseYy, 50, 50], 0)
        #recordPosition=[mouseX,mouseY]

def askaway():
    aasking=tk.messagebox.askyesnocancel("Check Start","Ready?")
    if(aasking==True):
        print("here we go then")
    elif (aasking==False):
        print("Ok....so quit already")
        sys.exit(0)
    else:#(assking == None):
        print("Canceling....")
        sys.exit(0)


recordXpos=[]
recordYpos=[]
recordSep=[]
r=[]
g=[]
b=[]
tt=0
op =[]
askaway()
tkscreentest()

playscreentest()
print("Program ended")
sys.exit(0)


#for t in range(199):
#    print("x -",recordXpos[t],recordSep[t],"y -",recordYpos[t])
#for q in range(199):
#    pygame.draw.rect(screen, [255, 255, 255], [recordXpos[t], recordYpos[t], 40, 10], 1)

# screen.fill([255,255,255])
# time.sleep(3)
# for i in range(199):
#     pygame.draw.rect(screen, [255, 255, 255], [recordXpos[i], recordYpos[i], 50, 50], 0)
# time.sleep(5)
#sys.exit(0)

#replayMoves()
#drawCircles()
# def drawCircles():
#     x=1
#     pygame.init()
#     screen=pygame.display.set_mode([640,480])
#     # screen.fill([0,0,255])
#     width =  pygame.mouse.get_pos()[0]
#     height = pygame.mouse.get_pos()[1]
#     print(width,height)
#     if(mouse.get_pressed() == True):
#         x=x+1
#     pygame.draw.circle(screen,[0,0,0],[150,150],80+x,0)
#
#     pygame.display.flip()
#     while True:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 sys.exit()
# pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
# pygame.draw.circle(screen, [255, 0, 0], [80, 400], 80 , 0)
# pygame.draw.circle(screen, [255, 0, 0], [80, 80], 80 , 0)
# pygame.draw.circle(screen, [255, 0, 0], [560, 80], 80 , 0)
# pygame.draw.circle(screen, [255, 0, 0], [560, 400], 80 , 0)
# screen.blit(x, (x.get_rect()))
# im.fill((120,120,120))
# pygame.draw.rect(screen, [128, 127, 128], [320,240,100,100], 0)
# def get_user_input(r,g,b):
#     #left = tk.mouse_buttons()
#     mouseX = pygame.mouse.get_pos()[0]
#     mouseY = pygame.mouse.get_pos()[1]
#     button_pressed = pygame.mouse.get_pressed()
#     fill=0
#     nofill=1
#
#    # print (button_pressed,"mmmoouuasee")
#     if(button_pressed[0] == True ):
#         print ("Left button pressed")
#         r=0
#         g=0
#         b=255
#         pygame.draw.circle(screen, [r, g, b], [80, 400], 80 , 0)
#         pygame.draw.rect(screen, [0, 0, 255], [mouseX, mouseY, 50, 50], 0)
#     else:
#         if(button_pressed[1] == True):
#             r = 0
#             g = 255
#             b = 0
#
#             print("Middle button pressed")
#             pygame.draw.circle(screen, [r, g, b], [80, 400], 80, 0)
#             pygame.draw.rect(screen, [0, 255, 0], [mouseX, mouseY, 50, 50], 0)
#         else:
#             if(button_pressed[-1] == True):
#                 r=255
#                 g=0
#                 b=0
#                 print("Right button pressed")
#                 pygame.draw.circle(screen, [r, g, b], [80, 400], 80, 0)
#                 pygame.draw.rect(screen, [255, 0, 0], [mouseX, mouseY, 50, 50], 0)
#     if(button_pressed[0] == True and button_pressed[-1] == True):
#         pygame.draw.rect(screen, [255, 255, 255], [mouseX, mouseY, 50, 50], 0)
#     return
