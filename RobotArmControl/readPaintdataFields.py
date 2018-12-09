from __future__ import with_statement

from io import *


def readInLine():
    cc = 0
    yy = 0
    xx = 0
    x = 0
    length = 0
    words = []
    fileInName = "paintSequence.psData"
    fileIn = open(fileInName, "r")
    data = fileIn.read()
    lineStart = 0
    lineFinish = 0
    inRecord = 0
    fields = 0
    field = []
    gotfield = False
    # numbers=fileIn.readline()
    # print("Read numbers :", numbers)
    for i in data:
        # x+=1
        # d = i.split(',')
        # ,i,x)
        if (i == ' '):
            print("begin value", length)
        elif (i == ','):
            print("end of value", length)
            length += 1
        # ,i,x)
        elif (i == '('):
            print("start of line")
            # ,i,x)
            lineStart += 1
        elif (i == ')'):
            print("end of line")
            # ,i,x)
            lineFinish += 1
        elif (i == '\n'):
            print("new line")
            inRecord += 1
        else:
            print("value - ", i, x)

        x += 1
    print(data)
    print(data[1:4], "from 0 to 5")
    print(len(data), "length")
    maxCount = (str(data[1:4]))
    for j in range(60):
        print(data[2:j + 39])
    print(maxCount, "Maxcount")
    if data[1:4] == '77':
        mxc = int(maxCount)
        print(mxc)
        print("yup")
    # print(maxCount)
    # print(data[2559:2562])
    print(x, length, inRecord, lineStart, lineFinish, fields)


# for t in data:
#     print((data[t:8]))

co = 1
r = []
g = []
b = []
mousex = []
mousey = []
brushSizel = []
brushsizew = []
count = []

with open("paintSequence.psData", "r") as filestream:
    num1 = filestream.readline()
    for line in filestream:
        lineIn = line.split()
        r.insert(co, str(lineIn[0]))
        g.insert(co, str(lineIn[1]))
        b.insert(co, str(lineIn[2]))
        mousex.insert(co, str(lineIn[3]))
        mousey.insert(co, str(lineIn[4]))
        brushSizel.insert(co, str(lineIn[5]))
        brushsizew.insert(co, str(lineIn[6]))
        count.insert(co, str(lineIn[7]))
        # print(r, "Red", g, "Green", b, "Blue", mousex, mousey, brushSizel, brushsizew, count)
        co += 1
    lastrecord = co - 1
    for u in range(lastrecord):
        cl1 = "Z"
        cl2 = "Z"
        cl3 = "Z"
        rd = ((r[u].strip("','")))
        gr = ((g[u].strip("','")))
        bl = ((b[u].strip("','")))
        msx = ((mousex[u].strip("','")))
        msy = ((mousey[u].strip("','")))
        bsl = ((brushSizel[u].strip("','")))
        bsw = ((brushsizew[u].strip("','")))
        cou = ((count[u].strip("',')")))
        if (rd == "0255"):
            print("red")
            cl1 = "red"
        if (gr == "0255"):
            print("green")
            cl2 = "green"
        if (bl == '0255'):
            print("blue")
            cl3 = "blue"
        # print(cl1, cl2, cl3, str(mousex[u]), mousey[u], brushSizel[u], brushsizew[u], count[u])
        print(cl1, cl2, cl3, "x", msx, "y", msy, "bsl", bsl, "bsw", bsw, "count", cou)
    # c = ((r[u].strip("(',')")))
    # # print(a.strip("'"), b ,"-",c,"-")
    # # d=int(c)*2
    # print(c)
    # if c.isdigit():
    #     print("yep")
    #     print(c * 2, " - ", c)
    # else:
    #     print("no")
