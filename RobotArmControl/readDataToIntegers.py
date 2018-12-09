from __future__ import with_statement
from io import *
import tkinter as tk
import tkinter.messagebox
import pygame
from pygame import *
import sys
pygame.init()



def playscreentest():
    screen = pygame.display.set_mode([640, 480])
    screen.fill([255, 255, 255])
    allofit = lastrecord
    if(allofit == 0):
        allofit = int(len(mousex))
    #allofit=lastrecord

    print(allofit)
    print("Doing play back")
    for yy in range(allofit):
        pygame.time.delay(20)
        pygame.display.flip()
        mouseXx = mousex[0:yy]
        mouseYy = mousey[yy]
        red = r[yy]
        green = g[yy]
        blue = b[yy]
        sz = brushSizel[yy]
        sy = brushsizew[yy]
        colordisplay=[red,green,blue]
        print(red, green, blue, mouseXx, mouseYy, sz, sy, yy)
        #a=int(msx.index(mouseXx,3,6))
       # print( a)

        pygame.draw.rect(screen, [0, 0, 255], [100, 100, 1, 10], 3)
        #pygame.draw.rect(screen, colordisplay, [mouseXx, mouseYy, sz, sy], 3)

    return


co = 1
r = []
g = []
b = []
mousex = []
mousey = []
brushSizel = []
brushsizew = []
count = []
lineMani=[]
screen = pygame.display.set_mode([640, 480])
with open("paintSequence.psData", "r") as filestream:
    num1 = filestream.readline()
    for line in filestream:
        lineIn = line.split(',')
        lineMani= lineIn    #insert(co, str(lineIn[0]))
        r.insert(co,lineIn[0:0])
        g.insert(co, lineMani[0:1])
        b.insert(co, lineMani[0:2])
        mousex.insert(co, lineMani[0:3])
        mousey.insert(co, lineMani[0:4])
        brushSizel.insert(co, lineMani[0:5])
        brushsizew.insert(co, lineMani[0:6])
        count.insert(co, lineMani[0:7])
        #pygame.draw.rect(screen, [r,g,b], [100, 100, brushSizel, brushsizew], 3)
        print(r, "Red", g, "Green", b, "Blue", mousex, mousey, brushSizel, brushsizew, count)
        co += 1
    lastrecord = co - 1
    for u in range(lastrecord):
        rd = (r[u])
        gr = (g[u])
        bl = (b[u])
        msx = (mousex[u])
        msy = (mousey[u])
        bsl = (brushSizel[u])
        bsw = (brushsizew[u])
        cou = (count[u])
        #pygame.draw.rect(screen, [r, g, b], [100, 100, bsl, bsw], 3)
        print(rd, gr, bl, "x", msx, "y", msy, "bsl", bsl, "bsw", bsw, "count", count)

        # if (rd == "0255"):
        #     print("red")
        #     cl1 = "red"
        # if (gr == "0255"):
        #     print("green")
        #     cl2 = "green"
        # if (bl == '0255'):
        #     print("blue")
        #     cl3 = "blue"
        # print(cl1, cl2, cl3, str(mousex[u]), mousey[u], brushSizel[u], brushsizew[u], count[u])

    playscreentest()
    # c = ((r[u].strip("(',')")))
    # # print(a.strip("'"), b ,"-",c,"-")
    # # d=int(c)*2
    # print(c)
    # if c.isdigit():
    #     print("yep")
    #     print(c * 2, " - ", c)
    # else:
    #     print("no")
# rd = ((r[u].strip("(,'")))
# gr = ((g[u].strip("','")))
# bl = ((b[u].strip("','")))
# msx = ((mousex[u].strip("','")))
# msy = ((mousey[u].strip("','")))
# bsl = ((brushSizel[u].strip("','")))
# bsw = ((brushsizew[u].strip("','")))
# cou = ((count[u].strip("',')")))