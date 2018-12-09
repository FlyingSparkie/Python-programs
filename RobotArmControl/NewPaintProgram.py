from __future__ import with_statement       ## used for file handling

import sys
import tkinter as tk
import tkinter.messagebox
from io import *

import pygame
from pygame import *

pygame.init()

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
                            #### printing some variables to console to debug
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
    #       use keys a, z, q and w and to resize rectangle
    #       problem is you have to keep mouse button pressed to see changes
    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == K_x:
                tt = yy - 1                                         ## stores max counted moves - not used tho
                finished = True                                     #### get out of loop exit program and console
            if event.type == pygame.KEYDOWN and event.key == K_a:
                zSize += 1
                record = True                                       ## record sizing element
            if event.type == pygame.KEYDOWN and event.key == K_z:
                zSize -= 1
                record = True                                       ## record sizing element
            if event.type == pygame.KEYDOWN and event.key == K_q:
                ySize -= 1
                record = True                                       ## record sizing element
            if event.type == pygame.KEYDOWN and event.key == K_w:
                ySize += 1
                record = True                                       ## record sizing element
        yy = yy + 1
        pygame.time.delay(20)
        x = x + x_speed
        if x > 480 or x < 0:
            x_speed = -x_speed
        pygame.display.flip()
        mouseX = pygame.mouse.get_pos()[0]                  ### mouse x position
        mouseY = pygame.mouse.get_pos()[1]                  ### mouse y position
        noPaint = -1                                        # No thickness = -1
        pygame.draw.rect(screen, [0, 0, 0], [mouseX, mouseY, 30, 30], noPaint)      ### set position but don't draw anything
        mouseX = pygame.mouse.get_pos()[0]                  ### get next x position
        mouseY = pygame.mouse.get_pos()[1]                  ### get next y position
        button_pressed = pygame.mouse.get_pressed()
        if (button_pressed[0] == True):         ## left button[0] middle button [1] right button[-1](end of button array)
            record = True                           ## record left mouse button elements - change colour to blue
            print("Left button pressed")
            rr = 0
            gg = 0
            bb = 255
            pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)          ## displays current colour in bottom left
            pygame.draw.rect(screen, [0, 0, 255], [mouseX, mouseY, zSize, ySize], 0)

        else:
            if (button_pressed[1] == True):
                record = True                       ## record middle button elements - change colour to green
                rr = 0
                gg = 255
                bb = 0
                print("Middle button pressed")
                pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)      ## displays current colour in bottom left
                pygame.draw.rect(screen, [0, 255, 0], [mouseX, mouseY, zSize, ySize], 0)
            else:
                if (button_pressed[-1] == True):
                    record = True                   ## record middle button elements - change colour to red
                    rr = 255
                    gg = 0
                    bb = 0
                    print("Right button pressed")
                    pygame.draw.circle(screen, [rr, gg, bb], [80, 400], 20, 0)  ## displays current colour in bottom left
                    pygame.draw.rect(screen, [255, 0, 0], [mouseX, mouseY, zSize, ySize], 0)
                else:
                    print("Doing nothing")
                    record = False                  ## don't record anything
        if (button_pressed[0] == True and button_pressed[-1] == True):       ##  both left and right buttons - simulates erase
            record = True
            rr = 255
            gg = 255
            bb = 255
            pygame.draw.rect(screen, [rr, gg, bb], [mouseX, mouseY, zSize, ySize], 0)
        recSizeZ.insert(yy, zSize)
        recSizeY.insert(yy, ySize)
        if (record == True):                        ### only store necessary variables
            separator = " - "                       ## not used in final data output - debugging
            op.insert(yy, operation)
            recordXpos.insert(yy, mouseX)
            recordSep.insert(yy, separator)
            recordYpos.insert(yy, mouseY)
            r.insert(yy, rr)
            g.insert(yy, gg)
            b.insert(yy, bb)
        print(operation, mouseX, mouseY)            ## debugging
        print("")
    return


def loadsequence():
    screen = pygame.display.set_mode([640, 480])
    screen.fill([100, 100, 100])
    co = 1
    r = []
    g = []
    b = []
    countit = []
    # lorp=tk.messagebox.askyesno("Play or load","load")
    # if lorp == True:
    print("loading sequence")
    with open("paintSequence.psData", "r") as filestream:           # open existing file of data
        num1 = filestream.readline()
        for line in filestream:
            lineIn = line.split(',')
            #for t in range(8):
                #print(lineIn[t], "record =",co,"field",t)          # displays records and fields for debugging
            r.insert(co,int(lineIn[0].strip("'('")))                # read data but no quote or brackets stuff
            g.insert(co,int(lineIn[1].strip(" '")))
            b.insert(co,int(lineIn[2].strip(" '")))
            recordXpos.insert(co,int(lineIn[3].strip(" '")))
            recordYpos.insert(co,int(lineIn[4].strip(" '")))
            recSizeZ.insert(co,int(lineIn[5].strip(" '")))
            recSizeY.insert(co,int(lineIn[6].strip(" '")))
            countit.insert(co,int(lineIn[7].strip(" ')\n")))
            #print(int(r[co]), int(g[co]), int(b[co]), int(recordXpos[co]), int(recordYpos[co]), 10, 10,3)  # debugging vars
            co += 1
        print("sequence loaded")
        print("Max record:",co)
        lastrecord = co - 1
        screen.fill([128, 128, 128])
        pygame.display.flip()
        for f in range(lastrecord):                     ## loop thru all records
            pygame.time.delay(20)
            pygame.display.flip()
            print(r[f], g[f], recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f])       #print records - debugging
            pygame.draw.rect(screen,[r[f],g[f],b[f]],[recordXpos[f],recordYpos[f],10,10],0) # draw whats loaded
        print("sequence finished")                      ## all recorded stuff drawn
        print(lastrecord,"records processed")
        doitagain=tk.messagebox.askyesno("Again","reload and play again")       ## play it again just for the hell of it
        if(doitagain == True):
            loadsequence()


def playsequence():
    #                               N.B sequence needs to be loaded first, otherwise blank is drawn to the screen
    #                               so it plays sequence from last paint session
    print("sequence playing")
    print("Max record:", co)
    lastrecord = co - 1
    screen.fill([128, 128, 128])
    pygame.display.flip()
    for f in range(lastrecord):
        pygame.time.delay(20)
        pygame.display.flip()               ## draw to screen otherwise nothing happens
        print(r[f], g[f], recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f])       #  debugging
        pygame.draw.rect(screen, [r[f], g[f], b[f]], [recordXpos[f], recordYpos[f], recSizeZ[f], recSizeY[f]], 0)
    print("sequence finished")
    print(lastrecord, "records processed")
    doitagain = tk.messagebox.askyesno("Again", "play again")       ## play it again just for the hell of it
    if (doitagain == True):
        playsequence()


def savesequence():
    saveit = tk.messagebox.askyesnocancel("SAVE", "defo Save it")
    if (saveit == True):
        #######        TODO  part here to get list of available files     TODO          ######
        fileOutName = "paintSequence.psData"
        fileOut = open(fileOutName, "w")
        allofit = int(len(recordXpos))
        pr = ""
        print("saving sequence")
        for yy in range(allofit):
            mouseXx = recordXpos[yy]                # get instances of saved variables
            mouseYy = recordYpos[yy]
            red = r[yy]
            green = g[yy]
            blue = b[yy]
            sz = recSizeZ[yy]
            sy = recSizeY[yy]
            c = yy
            #                           write variables to file, comma separated, but not normal strict csv
            #                           does away from single and double quotes - screws up otherwise 
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

                    # initialise global variables - no need to pass parameters to functions
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
    askaway()           # this the only point you can exit program, answer 'no' if you're ready otherwise continue with program
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

    #  these below fill out fields with leading 0's to make 4 digit code - not needed as fields are comma separated
# red = '%04d' % red
# green = '%04d' % green
# blue = '%04d' % blue
# mouseXx = '%04d' % mouseXx
# mouseYy = '%04d' % mouseYy
# sy = '%04d' % sy
# sz = '%04d' % sz
# yy = '%04d' % yy
                    #       some original data used for debugging
# saveString = ("color","r",red ,"g", green,"b,",blue , "x",mouseXx, "y",mouseYy, "size", sz, sy, "Entry",yy)
# saveString = red, green, blue, mouseXx, mouseYy, sz, sy, c
