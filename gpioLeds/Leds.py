
from tkinter import *
#from Tkinter import Tk
import tkinter.messagebox as TkmB
from tkinter import Button
from tkinter import Listbox


# import tkinter.Message as TkmM
def rf():
    print("here")
    button2 = Button(text="RIGHT", width=10, height=20)
    button2.pack()


def lf():
    button1 = Button(text="LEFT", height=10, width=20)
    button1.pack()

    root = Tk()


TkmB.showinfo("Window Title", "Just press")
answer = TkmB.askquestion("Question 1:", "No, yes")

if answer == "yes":
    print(TkmB.showinfo("Confuscious Says", "And the question was??"))
if answer == "no":
    print(TkmB.showinfo("Confuscious Says", "Wise choice"))
# listbox1 = Listbox("Confucious Says")
button1 = Button(text="Right", command=rf, height=10, width=20)
button2 = Button(text="Left", command=lf, height=10, width=20)

button1.pack()
button2.pack()
# listbox1.pack()
root.mainloop()
