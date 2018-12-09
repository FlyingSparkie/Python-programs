from __future__ import with_statement

import sys
import tkinter as tk
import tkinter.messagebox
from io import *

import pygame
from pygame import *

# mkeyboard = pynput.keyboard.Controller()


pygame.init()
##screen = pygame.display.set_mode([640, 480])
# screen.fill([0, 0, 255])

# root = tk.Tk()
x = 1
zSize = 10
ySize = 10


# root=Tk()
# root.mainloop()
# def replayMoves():
# get array of positions
# divide them into coordinates
# start animation

def paintscreentest():
    finished = False
    rr = 255
    gg = 255
    bb = 255
    screen = pygame.display.set_mode([640, 480])
    screen.fill([rr, gg, bb])
    # screen2 = pygame.display.set_mode([300, 200])
    # pygame.display.iconify()
    # screen2.fill([rr, 0, bb])
    # screen3 = pygame.display.set_mode([200, 200])
    # screen3.fill([0, gg, bb])
    x = 50
    x_speed = 10
    yy = 1
    operation = "Ready"
    ySize = 10
    zSize = 10
    # pygame.draw.rect(screen2, [0, 0, 0], [100,100, 10, 10], 0)
    currentsurface = pygame.display.get_surface()
    print(currentsurface)
    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == K_x:
                tt = yy - 1
                finished = True
            if event.type == pygame.KEYDOWN and event.key == K_a:
                zSize += 1
                record = True
            if event.type == pygame.KEYDOWN and event.key == K_z:
                zSize -= 1
                record = True
            if event.type == pygame.KEYDOWN and event.key == K_q:
                ySize -= 1
                record = True
            if event.type == pygame.KEYDOWN and event.key == K_w:
                ySize += 1
                record = True
        yy = yy + 1
        pygame.time.delay(20)
        x = x + x_speed
        if x > 480 or x < 0:
            x_speed = -x_speed
        pygame.display.flip()
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        noPaint = -1  # No thickness = -1
        pygame.draw.rect(screen, [0, 0, 0], [mouseX, mouseY, 30, 30], noPaint)
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        button_pressed = pygame.mouse.get_pressed()
        if (button_pressed[0] == True):
            record = True
            print("Left button pressed")
            rr = 0
            gg = 0
            bb = 255
            pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)
            pygame.draw.rect(screen, [0, 0, 255], [mouseX, mouseY, zSize, ySize], 0)

        else:
            if (button_pressed[1] == True):
                record = True
                rr = 0
                gg = 255
                bb = 0
                print("Middle button pressed")
                pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)
                pygame.draw.rect(screen, [0, 255, 0], [mouseX, mouseY, zSize, ySize], 0)
            else:
                if (button_pressed[-1] == True):
                    record = True
                    rr = 255
                    gg = 0
                    bb = 0
                    print("Right button pressed")
                    pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)
                    pygame.draw.rect(screen, [255, 0, 0], [mouseX, mouseY, zSize, ySize], 0)
                else:
                    print("Doing nothing")
                    record = False
        if (button_pressed[0] == True and button_pressed[-1] == True):
            record = True
            rr = 255
            gg = 255
            bb = 255
            pygame.draw.rect(screen, [rr, gg, bb], [mouseX, mouseY, zSize, ySize], 0)
        #
        # if(mouseX >= 80 and mouseX <=100 and mouseY>=400 and mouseY<=420):
        #     #pygame.draw.circle(screen, [0, 255, 0], [180, 400], 40, 0)
        #     pygame.draw.rect(screen, [rr, gg, bb], [240, 360, 50, 50],1 )
        # #screen.fill([255, 0, 255])
        # else:
        #     if (mouseX <= 80 and mouseX >= 100 and mouseY <= 400 and mouseY >= 420):
        #         pygame.draw.rect(screen, [0, 0, 0], [240, 360, 50, 50], 0)
        # pygame.draw.circle(screen, [255, 255, 0], [180, 400], 40, 0)
        # screen.fill([255,255,255])
        recSizeZ.insert(yy, zSize)
        recSizeY.insert(yy, ySize)
        if (record == True):
            separator = " - "
            op.insert(yy, operation)
            recordXpos.insert(yy, mouseX)
            recordSep.insert(yy, separator)
            recordYpos.insert(yy, mouseY)
            r.insert(yy, rr)
            g.insert(yy, gg)
            b.insert(yy, bb)
        print(operation, mouseX, mouseY)
        print("")
    return


def playscreentest():
    screen = pygame.display.set_mode([640, 480])
    screen.fill([255, 255, 255])
    allofit = lastrecord
    if (allofit == 0):
        allofit = int(len(recordXpos))
    # allofit=lastrecord

    print(allofit)
    print("Doing play back")
    for yy in range(allofit):
        pygame.time.delay(20)
        pygame.display.flip()
        mouseXx = recordXpos[yy]
        mouseYy = recordYpos[yy]
        red = r[yy]
        green = g[yy]
        blue = b[yy]
        sz = recSizeZ[yy]
        sy = recSizeY[yy]
        pygame.draw.rect(screen, [red, green, blue], [mouseXx, mouseYy, sz, sy], 0)
    return




def savesequence():
    saveit = tk.messagebox.askyesnocancel("SAVE", "defo Save it")
    if (saveit == True):
        fileOutName = "paintSequence.psData"
        fileOut = open(fileOutName, "w")
        allofit = int(len(recordXpos))
        # totalNum = '%04d' % allofit
        # fileOut.write("( " + str(totalNum) + ",)""\n")
        pr = ""
        print("saving sequence")
        for yy in range(allofit):
            mouseXx = recordXpos[yy]
            mouseYy = recordYpos[yy]
            red = r[yy]
            green = g[yy]
            blue = b[yy]
            sz = recSizeZ[yy]
            sy = recSizeY[yy]
            c = yy
            # red = '%04d' % red
            # green = '%04d' % green
            # blue = '%04d' % blue
            # mouseXx = '%04d' % mouseXx
            # mouseYy = '%04d' % mouseYy
            # sy = '%04d' % sy
            # sz = '%04d' % sz
            # yy = '%04d' % yy

            # saveString = ("color","r",red ,"g", green,"b,",blue , "x",mouseXx, "y",mouseYy, "size", sz, sy, "Entry",yy)
            saveString = red, green, blue, mouseXx, mouseYy, sz, sy, c
            fileOut.write(
                str(red) + "," + str(green) + "," + str(blue) + "," + str(mouseXx) + "," + str(mouseYy) + "," + str(
                    sz) + "," + str(sy) + "," + str(yy) + "\n")
            # fileOut.writelines(str(saveString))

        # fileOut.write(red + "-" + green + blue + mouseXx + mouseYy + sz + sy)
        print(fileOut, "EOF")
        fileOut.close()
        return
    elif (saveit == False):
        print("Not saving")
        return


def askaway():
    aasking = tk.messagebox.askyesno("Start", "Ready?")
    if (aasking == True):
        print("Continuing...............")
        return
    elif (aasking == False):
        print("....................Exiting")
        sys.exit(0)


recordXpos = []
recordYpos = []
recordSep = []
r = []
g = []
b = []
rload = []
gload = []
bload = []
tt = 0
op = []
rr=[]
recSizeY = []
recSizeZ = []
lastrecord = 0
while 1:
    askaway()
    aasking = tk.messagebox.askyesno("load play back", "load seq")
    if (aasking == True):
        print("Continuing....OK.....load......")
        loadsequence()
    elif (aasking == False):
        print("...............skip.....")
    aasking = tk.messagebox.askyesno("Paint away!", "paint something")
    if (aasking == True):
        print("Continuing....OK.....paint......")
        paintscreentest()
    elif (aasking == False):
        print("...............skip.....")
    aasking = tk.messagebox.askyesno("save play back", "save seq")
    if (aasking == True):
        print("Continuing....OK......save.....")
        savesequence()
    elif (aasking == False):
        print("...............skip.....")
    aasking = tk.messagebox.askyesno("play back", "Play seq")
    if (aasking == True):
        print("Continuing........OK....play......")
        playscreentest()
    elif (aasking == False):
        print(".....skip...............")

    print("Program ended")

#           Later to do...

# if event.type == pygame.KEYDOWN and event.key == K_c:
#     operation = "Circle"
# if event.type == pygame.KEYDOWN and event.key == K_r:
#     operation = "Rectangle"
# if event.type == pygame.KEYDOWN and event.key == K_e:
#     operation = "Ellipse"
# if event.type == pygame.KEYDOWN and event.key == K_l:
#     operation = "Line"
