#Exercise 1: Handling ZeroDivisionError

#Instructions:

#Write a program that takes two numbers as input from the user and divides the first number by the second number.
#Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

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