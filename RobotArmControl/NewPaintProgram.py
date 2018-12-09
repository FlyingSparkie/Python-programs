from __future__ import with_statement

import sys
import tkinter as tk
import tkinter.messagebox
from io import *

import pygame
from pygame import *

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
    x = 50
    x_speed = 10
    yy = 1
    operation = "Ready"
    ySize = 10
    zSize = 10
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


# def playscreentest():
#     screen = pygame.display.set_mode([640, 480])
#     screen.fill([255, 255, 255])
#     allofit = lastrecord
#     if (allofit == 0):
#         allofit = int(len(recordXpos))
#     # allofit=lastrecord
#         screen.fill([128, 128, 128])
#         pygame.display.flip()
#         for f in range(lastrecord):
#             pygame.time.delay(20)
#             pygame.display.flip()
#             print(r[f], g[f], recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f])
#             pygame.draw.rect(screen,[r[f],g[f],b[f]],[recordXpos[f],recordYpos[f],10,10],0)
#     print(allofit)
#     print("Doing play back")
    # for yy in range(allofit):
    #     pygame.time.delay(20)
    #     pygame.display.flip()
    #     mouseXx = recordXpos[yy]
    #     mouseYy = recordYpos[yy]
    #     red = r[yy]
    #     green = g[yy]
    #     blue = b[yy]
    #     sz = recSizeZ[yy]
    #     sy = recSizeY[yy]
    #     pygame.draw.rect(screen, [red, green, blue], [mouseXx, mouseYy, sz, sy], 0)
    #return

def loadsequence():
    screen = pygame.display.set_mode([640, 480])
    screen.fill([100, 100, 100])
    co = 1
    # loadString = []
    # rload = []
    # gload = []
    # bload = []
    r = []
    g = []
    b = []
    # mousex = []
    # mousey = []
    # brushSizel = []
    # brushsizew = []
    countit = []
    # lorp=tk.messagebox.askyesno("Play or load","load")
    # if lorp == True:
    print("loading sequence")
    with open("paintSequence.psData", "r") as filestream:
        num1 = filestream.readline()
        for line in filestream:
            lineIn = line.split(',')
            #for t in range(8):
                #print(lineIn[t], "record =",co,"field",t)
            r.insert(co,int(lineIn[0].strip("'('")))
            g.insert(co,int(lineIn[1].strip(" '")))
            b.insert(co,int(lineIn[2].strip(" '")))
            recordXpos.insert(co,int(lineIn[3].strip(" '")))
            recordYpos.insert(co,int(lineIn[4].strip(" '")))
            recSizeZ.insert(co,int(lineIn[5].strip(" '")))
            recSizeY.insert(co,int(lineIn[6].strip(" '")))
            countit.insert(co,int(lineIn[7].strip(" ')\n")))
            #print(int(r[co]), int(g[co]), int(b[co]), int(recordXpos[co]), int(recordYpos[co]), 10, 10,3)
            co += 1
        print("sequence loaded")
        print("Max record:",co)
        lastrecord = co - 1
        screen.fill([128, 128, 128])
        pygame.display.flip()
        for f in range(lastrecord):
            pygame.time.delay(20)
            pygame.display.flip()
            print(r[f], g[f], recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f])
            pygame.draw.rect(screen,[r[f],g[f],b[f]],[recordXpos[f],recordYpos[f],10,10],0)
        print("sequence finished")
        print(lastrecord,"records processed")
        doitagain=tk.messagebox.askyesno("Again","reload and play again")
        if(doitagain == True):
            loadsequence()


def playsequence():
    print("sequence playing")
    print("Max record:", co)
    lastrecord = co - 1
    screen.fill([128, 128, 128])
    pygame.display.flip()
    for f in range(lastrecord):
        pygame.time.delay(20)
        pygame.display.flip()
        print(r[f], g[f], recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f])
        pygame.draw.rect(screen, [r[f], g[f], b[f]], [recordXpos[f], recordYpos[f], 10, 10], 0)
    print("sequence finished")
    print(lastrecord, "records processed")
    doitagain = tk.messagebox.askyesno("Again", "play again")
    if (doitagain == True):
        playsequence()


def savesequence():
    saveit = tk.messagebox.askyesnocancel("SAVE", "defo Save it")
    if (saveit == True):
        #######         part here to get list of available files
        fileOutName = "paintSequence.psData"
        fileOut = open(fileOutName, "w")
        allofit = int(len(recordXpos))
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
            fileOut.write(
                str(red) + "," + str(green) + "," + str(blue) + "," + str(mouseXx) + "," + str(mouseYy) + "," + str(
                    sz) + "," + str(sy) + "," + str(yy) + "\n")
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
    aasking = tk.messagebox.askyesno("load play back", "load sequence")
    if (aasking == True):
        print("Continuing....OK.....load......")
        loadsequence()
    elif (aasking == False):
        print("...............skip loading.....")
    aasking = tk.messagebox.askyesno("Paint away!", "paint something")
    if (aasking == True):
        print("Continuing....OK.....paint......")
        paintscreentest()
    elif (aasking == False):
        print("...............skip painting.....")
    aasking = tk.messagebox.askyesno("save play back", "save sequence")
    if (aasking == True):
        print("Continuing....OK......save.....")
        savesequence()
    elif (aasking == False):
        print("...............skip saving.....")
    aasking = tk.messagebox.askyesno("play back", "Play sequence")
    if (aasking == True):
        print("Continuing........OK....play......")
        playsequence()
    elif (aasking == False):
        print("...............skip playing.........")
    # not ended but re-looped
    print("Program ended")

# red = '%04d' % red
# green = '%04d' % green
# blue = '%04d' % blue
# mouseXx = '%04d' % mouseXx
# mouseYy = '%04d' % mouseYy
# sy = '%04d' % sy
# sz = '%04d' % sz
# yy = '%04d' % yy

# saveString = ("color","r",red ,"g", green,"b,",blue , "x",mouseXx, "y",mouseYy, "size", sz, sy, "Entry",yy)
# saveString = red, green, blue, mouseXx, mouseYy, sz, sy, c
