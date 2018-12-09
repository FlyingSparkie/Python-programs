import random
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pygame
from time import sleep


pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([0,0,255])
x = 1

top = tk.Tk()
root = tk.Tk()

embed = tk.Frame(root,width = 200, height = 300)
embed.grid(columnspan = (600), rowspan = (400))
embed.pack(side = LEFT)
aButton = tk.Button(top, text = "click", fg = "Blue")
bButton = tk.Radiobutton()
cButton = tk.Checkbutton()
dButton = tk.Button(top, text = "press here", fg = 'Red')
ebutton = tk.Button(embed, text = "click here", bg = "Red")
# fbuttonFrame = Frame(top, width = (100), height = (100))
fbutton = tk.Button(embed, text = 'there', fg = "Green", width = 30, height = 4)

aButton.pack()
bButton.pack()
cButton.pack()
dButton.pack()
fbutton.pack()
print(str(aButton), bButton, cButton, dButton)
for a in range(5):
    b=str(a)
    sleep(1)
    font = pygame.font.SysFont("comicsansms", 36)
    s=font.render("fonty mython" + b,True,(255,255,0))
    screen.blit(s, (20,200))
    pygame.display.flip()
   # pygame.display.flip()
    font = pygame.font.SysFont("comicsansms", 36)
    s = font.render("                    ", True, (0, 0, 0))
    screen.blit(s,(20,200))
    pygame.display.flip()
    pygame.display.update()
# sleep(3)
# screen.blit(x, x.get_rect())
# for t in range(2):
    # e=str(t)
    # fbu = tk.LabelFrame(None, text="Enter value", bg="Red")
fbutton = tk.Button(top, text = "here", fg = "Blue", width = 30, height = 3)
if(cButton == True):
    print("checked")
else:
    print("no check")
fbutton.update()
fbutton.pack()

def there():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update()

there()
mainloop()
print("program exited")