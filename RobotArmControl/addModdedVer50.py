from time import sleep
import numpy
import time
import random
t = []
operQ = []
sideQ = []
partQ = []
degQ = []
#cc=1
#seqQ = 0

def display_current_selection():
    print ("this will print current selection and filters in a window")
    print("possible animation of current process??")
    print(t)
    return


def getOperations():
    #ti=time.gmtime()
    rnd=(int(20*random.random()))
    print (rnd)
    #seqQ = int(input("How many separate operations are you doing?:"))
    seqQ = rnd
    # seqCount=3
    # t[]=t[seqCount]
    cc = 1
    # allofit=[10]
    # seqtodo=[cc]
    r = 0
    question1 = "Unanswered Q1"
    question2 = "Unanswered Q2"
    while cc <= seqQ:
        counter = cc
        print("currently -",t)
        #operation = input("Seq:{0}: What do you want to do ([r]otate, [b]end, [t]wist, [g]rab): ".format(cc))
        operation = int(4*random.random())
        # operation = "rotate"
        # print(sys.version)
        # while operation != 'r' and operation != 'b' and operation != 't' and operation != 'g':
        # invalid operation
        #    print("You must enter a valid operation(r,b,t,g)")
        #side = input("Seq:{0}: [l]eft or [r]ight".format(cc))
        side = int(2*random.random())
        #if(side == ""):
        #    side = "*"
        # side = "left"
        #part = input("Seq:{0}: [s]houlder, [a]rm, [h]hand".format(cc))
        part = int(3*random.random())
        #if(part == ""):
         #   part = "*"
        # part = "shoulder"
        #degrees = input("Seq:{0}: Enter degrees".format(cc))
        degrees = int(179*random.random())
        #if(degrees == ""):
         #   degrees = "*"
        # degrees = 45
        operQ.insert(cc, operation)
        sideQ.insert(cc, side)
        partQ.insert(cc, part)
        degQ.insert(cc, degrees)
        t.insert(cc,operQ)
        t.insert(cc,sideQ)
        t.insert(cc,partQ)
        t.insert(cc,degQ)
        display_current_selection()
        # print(allW," - ","counted", cc)
        cc = cc + 1
    seqQ = cc


getOperations()
rep=int(int(len(operQ)))
for i in range(int(len(operQ))):
#for i in range(cc):
    if (sideQ[i] == 1):
        sideQ[i] = "Left"
    else:
        if (sideQ[i] == 0):
            sideQ[i] = "right"
    if (operQ[i] == 0):
        operQ[i] = "Rotate"
    else:
        if (operQ[i] == 1):
            operQ[i] = "Bend"
        else:
            if (operQ[i] == 2):
                operQ[i] = "Twist"
            else:
                if (operQ[i] == 3):
                    operQ[i] = "Grab"
    if (partQ[i] == 0):
        partQ[i] = "shoulder"
    else:
        if (partQ[i] == 1):
            partQ[i] = "arm"
        else:
            if (partQ[i] == 2):
                partQ[i] = "hand"
    t[i]=(i," - ", operQ[i], sideQ[i], partQ[i], degQ[i], " degrees")
    print(i," - ", operQ[i], sideQ[i], partQ[i], degQ[i], " degrees")
    #rep=i
    #print(t[i])


print("All finished")
#for j in range(int(len(t))):
for j in range(rep):
    print(j," - ",t[j], " -")

#for k in range(t):                 this won't work - t is list
#    print(t)

#  if(operation == "r"):
#      question1 = "Enter r for rotate right shoulder l for left:"
#      #question2 = "Enter degrees 0-180"
#      r = 1
#  elif (operation == "b"):
#      question1 = "Enter r bend right arm l for left:"
#      #question2 = "Enter degrees 0-100"
#      r = 2
#  elif (operation == "t"):
#      question1 = "Enter r for twist right hand l for left:"
#      #question2 = "Enter degrees 0-180"
#      r = 3
#  elif (operation == "g"):
#      question1 = "Enter r grab with right hand l for left:"
#      #question2 = "Enter degrees 0-180"
#      r = 4
# # operationQ.append(r)

# num1 = (input(question1))
# num2 = (input("Enter degrees 1- 180"))

# num1 = input(question1)
# if(num1[cc] == 'l'):
#     num1Q = 1
#     print("left")
# else:
#     num1Q = 2
#     print("right")
#
# operationQ.append(r)
# firstQ.append(num1Q)
# secondQ.append(num2)
# allQ.append(operationQ + firstQ + secondQ)


# if r == 1:
#     if (firstQ == 1):
#         todoQ = "Rotating left shoulder :" , secondQ
#     else:
#         todoQ = "Rotating right shoulder" , secondQ
#     todoQpass.append(todoQ)
# elif r == 2:
#     if (firstQ == 1):
#         todoQ = "Bending left elbow" , secondQ
#     else:
#         todoQ = "Bending right elbow" , secondQ
#     todoQpass.append(todoQ)
# elif  r == 3:
#     if (firstQ == 1):
#         todoQ = "Twisting left hand" , secondQ
#     else:
#         todoQ = "Twisting right hand" , secondQ
#     todoQpass.append(todoQ)
# elif r == 4:
#     if (firstQ == 1):
#         todoQ = "grab with left hand" , secondQ
#     else:
#         todoQ = "grab with right hand" , secondQ
#     todoQpass.append(todoQ)
# print(todoQpass," - ", firstQ)

# num1Q=list()
# firstQ=list()
# secondQ=list()
# #todoQ=list()
# todoQpass=list()
# operationQ = list([])

# allQ=list()
# allofit=list()
# #seqCount = createSequence()
# #print("doing ", seqCount, "sequences")
# getOperations()
# print("All finished")
# length_of_list = int(len(allQ))
# for i in allQ:
#     print (i)
# print(allQ[length_of_list-4],allQ[length_of_list-3],allQ[length_of_list-2],allQ[length_of_list-1])
# howmany=int(len(firstQ))
# howmany = seqCount
# print("How many =", int(len(firstQ)))
# howmany = int(len(firstQ))
# #print(r)
# m = 0
# for i in firstQ:
#     if(firstQ == 1):
#         print("left left")
#     else:
#         print("right right")
#
#     #                           put if checks for left or right
# for j in secondQ:
#     print(j, "degrees")
#
# for k in todoQpass:
#     print("Instruction - ",k)
#
# print("full strings")
# for t in num1Q:
#     print(t)
#
# for m in range(howmany):
#     #print(allQ[m],m)
#     if(firstQ[m]==1):
#         hand ="left"
#     else:
#         hand = "right"
#     print(" -", todoQpass[m],secondQ[m],"degrees", hand, "hand" )

# print("str", outstring, "count", a, "num", b, "num", c, "op", operation, "sel", d)
# i =- 1
# for i in range(1):
#    print(outstring)
# print(count)
