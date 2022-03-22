number1=int(input("enter first no. "))
if (number1 % 3 ==0 and number1 % 5 ==0):
    print("fizz buzz")
elif (number1 % 3 ==0):
    print("fizz")
elif (number1 %5 ==0):
    print("buzz")
else:
    print(number1)
    


