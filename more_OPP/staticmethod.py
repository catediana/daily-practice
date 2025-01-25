#Exercise 2: Static Method for Utility Calculation Instruction:

#Create a class Calculator with static methods for basic mathematical operations like addition and multiplication.
#Implement static methods add() and multiply() to perform these operations.


#creating the calculator class
class Calculator:

#defining a tatic method for adding number   
    @staticmethod
    def add(x,y):
        return x + y
#defining a tatic method for mutiplying two number
    @staticmethod
    def multiply( a,b):
        return a * b

#calling the methods
print(Calculator.add(5 , 7))    
print(Calculator.multiply(5 ,10))    