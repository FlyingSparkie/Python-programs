from __future__ import with_statement

#import tkinter as tk
#import tkinter.messagebox

import pygame
from pygame import *
import io
from io import *
from sys import *


def loadsequence():
    #loadfileQuestion = tk.messagebox.askyesnocancel("Loading a data file", "Continue")
    inXpos = []
    inYpos = []
    inYposVal = 0
    red = []
    green = []
    blue = []
    recsy = []
    recsz = []
    loadfileQuestion=True
    if (loadfileQuestion == True):
        print("loading sequence")
        fileInName = "paintSequence.psData"
        fileIn = open(fileInName, "r")
        howmanySequences=0
        yy=0
        stringIn=[]
        inval=[]
        counter =1
        with open("paintSequence.psData") as f:
            #recordYpos.insert(yy, mouseY)
            for line in f:
                #stringIn=line
                stringIn.insert(counter,line)
                #print (f)
                #print(stringIn[counter])
                counter +=1
                #print(line)

            print(counter)

            print(" - ", stringIn[1],stringIn[5])
            print(" - ", stringIn[1][5])
            sizeof=int(len(stringIn[1]))
            howmanyper=sizeof-int(len(stringIn))
            print("there are ",sizeof, "entries and ", howmanyper, "fields each ", counter," counted ")
            #print(int(len(stringIn[1])))


        # fileIn.read((howmanySequences))
        # while 1:            #(fileIn.read!= "EOF"):
        #     fileIn.read((inYposVal))
        #     print(inYposVal)
        #     yy = yy+1
            #loadString =""
            #fileIn.read([color],[r,g,b]))
            # recordXpos[yy] = inXpos
            # recordYpos[yy] = inYpos
            # r[yy] = red
            # g[yy] = green
            # b[yy] = blue
            # recSizeZ[yy] = recsz
            # recSizeY[yy] = recsy

        # fileOut.write(red + "-" + green + blue + mouseXx + mouseYy + sz + sy)
        #print(fileOut, "EOF")
        fileIn.close()


loadsequence()

    # elif (saveit == False):
    #     print("Not saving")
    #     return
# fileIn.read(incolor,inrlabel,red[yy] ,inglabel, green[yy],inblabel,blue[yy], xlabel,inXpos[yy], ylabel,inYpos[yy], sizelabel, recsz[yy], recsy[yy], yin)
       #    allofit = int(len(recordXpos))
        #   for yy in range(allofit):
        #     incolor=""
        #     inrlabel=""
        #     inglabel=""
        #     inblabel=""
        #     xlabel=""
        #     ylabel=""
        #     sizelabel=""

