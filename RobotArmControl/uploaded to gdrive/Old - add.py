import sys
import array as seq

#outstring = [[]]
sequence = [()]

def rotateShoulder(num1, num2):
    return


def bendElbow(num1, num2):
    return


def twistWrist(num1, num2):
    return


def grab(num1, num2):
    return


def createSequence():
   # sequenceCount = 0
    countSeq = int(input("How many separate operations are you doing?:"))
    return countSeq


def getOperations(seqCount):
    cc = 1
   # global outstring
   # count = b
   # operation = a
   # r = c
    while cc <= seqCount:
        operation = input("What do you want to do ([r]otate, [b]end, [t]wist, [g]rab): ")
        #print(sys.version)
        while operation != 'r' and operation != 'b' and operation != 't' and operation != 'g':
            # invalid operation
            print("You must enter a valid operation(r,b,t,g)")

        if(operation == "r"):
            question1 = "Enter 0 for right shoulder anything else for left:"
            question2 = "Enter degrees 0-180"
            num1 = int(input(question1))
            num2 = int(input(question2))
            r=1
        elif (operation == "b"):
            question1 = "Enter 0 for bend right arm anything else for left:"
            question2 = "Enter degrees 0-100"
            num1 = int(input(question1))
            num2 = int(input(question2))
            r=2
        elif (operation == "t"):
            question1 = "Enter 0 for twist right hand anything else for left:"
            question2 = "Enter degrees 0-180"
            num1 = int(input(question1))
            num2 = int(input(question2))
            r=3
        elif (operation == "g"):
            question1 = "Enter 0 for grab with right hand anything else for left:"
            question2 = "Enter degrees 0-180"
            r=4
            num1 = int(input(question1))
            num2 = int(input(question2))
        cc = cc + 1
       # n1=num1
       # n2=num2
        #return count, num1, num2, operation, r
        return (operation, num1, num2, r)

def selectionProcess(outstring, operation, num1, num2):
    # operation = a
    # num1 = b
    # num2 = c
    # outstring = d
    if operation == "r":
        if (num1 != 0):
            outstring = ["Rotating left shoulder" , num2 , " degrees"]
        else:
            outstring= ["Rotating right shoulder" , num2 , " degrees"]
        #print(rotateShoulder(num1, num2))
    elif operation == 'b':
        if (num1 != 0):
            outstring = str({"Bending left elbow" , num2 , " degrees"})
        else:
            outstring = str({"Bending right elbow" , num2 , " degrees"})
        #print(bendElbow(num1, num2))
    elif  operation == "t":
        if (num1 != 0):
            outstring = str({"Twisting left hand" , num2 , " degrees"})
        else:
            outstring = str({"Twisting right hand" , num2 , " degrees"})
        #print(twistWrist(num1, num2))
    elif operation == "g":
        if (num1 != 0):
            outstring = str({"grab with left hand" , num2 , " degrees"})
        else:
            outstring = str({"grab with right hand" , num2 , " degrees"})
    print((outstring))
   # return operation,num1,num2,outstring
    return (outstring,operation,num1,num2)


def main():
    outstring = ""
    operation = ""
    a = ""
    b = 0
    c = 0
    d = ""
    seqCount = createSequence()
    print("doing ", seqCount, "sequences")
    getOperations(seqCount)
    selectionProcess(a, b, c, d)
    #print ("string begin",outstring[0])
    #print("string mid", outstring[1])
    #print ("string end",outstring[-1])
    print("All finished", a , b, c, d)
    print("str", outstring, "count", a, "num", b, "num", c, "op", operation, "sel", d)
    #i =- 1
    #for i in range(1):
    #    print(outstring)
    #print(count)


main()