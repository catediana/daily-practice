num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))


# handling the error if it might occur
try:
    if num2 == 0:
       print("ZerroDivission error, a number cannot be divided by zero")
    else:
        results = num1/num2
        print(results)

    
finally:
    print("bye")