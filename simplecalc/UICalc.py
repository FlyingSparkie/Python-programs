from Tkinter import *


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=2, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __int__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        master.title("Calculator")
        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display, justify='center', bd=30, bg="powder blue") \
            .pack(side=TOP, expand=YES, fill=BOTH)


if __name__ == '__main__':
    app().mainloop()
