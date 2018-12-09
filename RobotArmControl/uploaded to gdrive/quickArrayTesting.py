# d=int(input("enter something int"))
# e=int(input("enter something else int"))
# yy=[e]
# y=d
y=67
yy=98

x = [[2,6,9],[1,7,3,4,5, 'helper', 'bug']]

print(x[1][6]) # x[second index][position in index]
print(x[0][2]) # x[first index][position in index]
print(x[1][1])
x.insert(y,yy)
print(x)
cc=1
#counter=int(input("enter how many"))
memo=[]
memo2=[]
memo3=[]

#for i in range (10):
isint = False
# target_int = 0
countera=0
while isint == False:
    counter = input("How many integers>:")
    try:
        counter = int(counter)
        countera = counter
        isint = True

        #return countera
    except ValueError:
        isint = False
        print("number is needed")


while cc <= countera:
    # operation = input("Seq:{0}: What do you want to do ([r]otate, [b]end, [t]wist, [g]rab): ".format(cc))
    x=int(input("enter no.{0} \n".format(cc)))
    x=int(x)
    memo.insert(cc,x)
    y=input("enter t,b,g for .{0} \n".format(cc))
    memo2.insert(cc,y)
    z=input("Enter degs {0}\n".format(cc))
    memo3.insert(cc,z)
    cc+=1
rcount=cc-1
print(memo)
cou=1
ind=x
for t in range(rcount):
    print(t," - ",memo[t], memo2[t],memo[t])