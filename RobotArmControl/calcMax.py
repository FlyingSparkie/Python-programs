import sys


def getCount():
    isint = False
    #target_int = 0
    while isint == False:
        target_int = input("How many integers>:")
        try:
            target_int = int(target_int)
            isint = True
            countera=target_int
            return countera
        except ValueError:
            isint = False
            print("number is needed")
    #return countera


def getIntegers(count):
    counterc = 0
    isint = False
    target_int = 0
    #counterc = count
    while counterc < count:
        while isint == False:
            x = input("Enter number {0}: ".format(counterc + 1))
            quesy = "this a string "
            try:
                x = int(x)
                y = x + 5
               # target_int = int(target_int)
                isint = True
                ints.append(x)
                yints.append(quesy+str(y))
                #counterc = counterc + 1
            except ValueError:
                isint = False
                print("number is needed")
            print("int entered")
        print("int check valid")
        isint = False
        counterc +=1

    print("entries finished")

    #return counterb

ints = list()
yints = list()
#count = 0
#countera=0
counterb=0
counter = 0
isint = False
countera=getCount()
count = countera
print(count, counterb)
getIntegers(count)
dints = int(len(ints))
for i in ints:
    print("x:",i)
print("first nums done")
for ii in range(dints):
    print("new x: ", ints[ii])
    print("new y: ", yints[ii])
