a=0
b=int(input("enter the no of rows"))
for lines in range(1,b+1):
    for spaces in range(0,b-lines):
        print(" ",end="")
    for stars in range(0,a+lines):
        print("*",end="")
    a=a+1
    print ("\r")