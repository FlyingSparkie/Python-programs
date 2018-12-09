import random
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pygame, sys
from pygame import *
from time import sleep
import pynput.keyboard


#           global variables here
pygame.init()

screen=pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
startcoord=0
finishcoord=0
root=tk.Tk()


def drawRectangle():

    pygame.draw.rect(screen, [0, 255, 0], [100, 100, 60, 50], 1)
    pygame.draw.rect(screen, [0, 255, 0], [200, 200, 60, 50], 1)
    #pygame.draw.line(screen, [0, 255, 0], 100, 150, 1)
    pygame.draw.rect(screen, [0, 255, 0], [150, 100, 60, 50], 1)
    pygame.draw.rect(screen, [0, 255, 0], [100, 100, 60, 50], 1)
    #pygame.draw.line(screen, [255,0,0], 10,30)
    #pygame.draw.rect(screen, [0, 0, 255], [mouseX, mouseY, 50, 50], 0)
    return


def moveXYDirection():
    print("move X and Y")
    return


def moveZ():
    print("Move in Z")
    return


def getCoords(a):
    #startcoord=a
    #finishcoord=a
    if(a==1):
        mouseX = pygame.mouse.get_pos()[0]
        startpos = pygame.mouse.get_pos()[1]
        coord1 = (mouseX, startpos)
        print("start - ", coord1)
        return coord1
    if (a==2):
        mouseY = pygame.mouse.get_pos()[0]
        finishpos = pygame.mouse.get_pos()[1]
        coord2 = (finishpos,mouseY)
        print ("finish - ", coord2)
        return coord2


def getfinishCoord():
   # mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    finishpos = pygame.mouse.get_pos()[1]
    coord2 = (mouseY, finishpos)
    print(coord2)
    return coord2


def drawit():
    finished = False
    x=0
    y=0
    pygame.mouse.set_pos(x, y)
    #pygame.draw.rect(screen, [0,255,0], [100,100,60,50],1)
    while finished == False:
        coord1 = 0
        coord2 = 0
        drawyet=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == K_x:
                sys.exit()
                #finished = True
            #if event.type == pygame.KEYDOWN and event.key == K_l:
            #if(mouse.get_pressed()==True):
            startcoord=0
            if(mouse.get_pressed()[0] == True):
                startcoord=1
                #if (mouse.get_rel()[0] == True):
                coord1=getCoords((startcoord))
                drawyet = False

                #print("coord 1 - ",coord1, mouse.get_rel()[0])
                if(mouse.get_pressed()[-1] == True and drawyet==False):
                    finishcoord=2
                    #if(mouse.get_rel()[1] == True):
                    coord2=getCoords((finishcoord))
                    drawyet = True

                #print ("coord 2 - ", coord2, mouse.get_rel()[1])
            if(drawyet==True):
                print(coord1, coord2)
                #pygame.draw.line(screen, (0, 255, 0), coord1, coord2)
                drawyet=False
            #print(coord1, coord2)
        pygame.display.flip()


drawit()
#drawRectangle()
#moveZ()
#moveXYDirection()
#sys.exit(0)
#
# mouseX = pygame.mouse.get_pos()[0]
# mouseY = pygame.mouse.get_pos()[1]
# mpos = [mouseX, mouseY]
# coord1 = [mouseX, mouseY]
# coord2 = [mouseX, mouseY]
# # startx = [mouseX,0]
# # finishy=[0,mouseY]
# print(mouseX, mouseY)
# firstcoord = True
# if (mouse.get_pressed()[0] == True):
#     mouseX = pygame.mouse.get_pos()[0]
#     mouseY = pygame.mouse.get_pos()[1]
#     # startcoord = getStartCoord()
#     coord1 = (mouseX, mouseY)
#     firstcoord = True
# if (mouse.get_pressed()[-1] == True and firstcoord == False):
#     mouseX2 = pygame.mouse.get_pos()[0]
#     mouseY2 = pygame.mouse.get_pos()[1]
#     mpos = pygame.mouse.set_pos(mouseX, mouseY)
#     # fincoord = getfinishCoord()
#     coord2 = (mouseX2, mouseY2)
#     pygame.draw.line(screen, (0, 255, 0), coord1, coord2)
#     print(coord1, " - ", coord2, " - ", mpos, "-")
#     firstcoord = False
#
# # startpos = pygame.mouse.get_pos()[0]
# ## coord1 = (mouseX + 1, startpos + 1)
# # pygame.draw.line(screen, (0, 255, 0), startxy, startxy)
# # print(startxy,coord1)
# # pygame.draw.line(screen, (0, 255, 0),coord1, coord2)
#
# # finishpos = pygame.mouse.get_pos()[1]
# # coord2 = (mouseY + 1, finishpos + 1)
# # pygame.draw.line(screen, (0, 255, 0), startxy, coord2)
# # print(startxy, coord2)
# # pygame.draw.line(screen, (0, 255, 0), coord1, coord2)
# # pygame.draw.line(screen, (0, 255, 0), coord2,y)
# # coord1 = (mouseX, startr)
# # coord2 = (mouseY, startf)
# # pygame.draw.rect(screen, [128, 127, 128], [mouseX, mouseY, 50, 50], 1)
# # pygame.draw.line(screen, (0, 255, 0), coord1, coord2)