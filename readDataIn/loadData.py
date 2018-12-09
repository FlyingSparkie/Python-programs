from __future__ import with_statement
import io
import sys
import tkinter as tk
import tkinter.messagebox
from io import *

import pygame
from pygame import *
pygame.init()



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
        doitagain=tk.messagebox.askyesno("Again","run again")
        if(doitagain == True):
            loadsequence()


def playsequence():
    screen = pygame.display.set_mode([640, 480])
    screen.fill([255, 255, 255])
    allofit = lastrecord

    #allofit=lastrecord

    print(allofit)
    print("Doing play back")
    for yy in range(200):
        pygame.time.delay(20)
        pygame.display.flip()
        mouseXx = recordXpos[yy]
        mouseYy = recordYpos[yy]
        red = r[yy]
        green = g[yy]
        blue = b[yy]
        sz = recSizeZ[yy]
        sy = recSizeY[yy]
        print(red, green, blue, mouseXx, mouseYy, sz, sy, yy)

        #pygame.draw.rect(screen, [int(red),int(green),int(blue)], [int(mouseXx), int(mouseYy), int(sz), int(sy)], 3)



loadsequence()
#playsequence()
