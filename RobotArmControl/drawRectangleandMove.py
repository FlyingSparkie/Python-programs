from pygame import *
import tkinter as tk
import tkinter.messagebox
#from tkinter import *
import pynput
import pygame,sys
import time

pygame.init()

screen=pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
root=tk.Tk()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == K_x:
            sys.exit()
        #if (mouse.get_pressed() == True):
    moveX = pygame.mouse.get_pos()[0]
    moveY = pygame.mouse.get_pos()[1]
    button_pressed = pygame.mouse.get_pressed()
    if (button_pressed[0] == True):
        print("Left button pressed")
        pygame.draw.rect(screen, [0, 255, 255], [moveX, moveY, 20, 20], 0)
    else:
        print("Doing nothing")
        #pygame.draw.rect(screen,[0,0,0],[moveX, moveY,20,20],1)


   # pygame.draw.rect(screen, [0, 255, 0], [moveX,moveY, 20, 20], 0)
    #pygame.draw.rect(screen, [0, 255, 0], [200, 200, 60, 50], 1)
    # pygame.draw.line(screen, [0, 255, 0], 100, 150, 1)
    #pygame.draw.rect(screen, [0, 255, 0], [150, 100, 60, 50], 1)
    #pygame.draw.rect(screen, [0, 255, 0], [100, 100, 60, 50], 1)
    # pygame.draw.line(screen, [255,0,0], 10,30)
    pygame.display.flip()