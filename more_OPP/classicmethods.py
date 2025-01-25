#Exercise 1: Class Methods for Counting Instances Instruction:

#Create a class Book with a class variable total_books to count the number of book instances created.
#Implement a class method display_total_books() to display the total number of books created.


#creating the book class
class Book:
    total_books = 0
#defining a method which takes book_number as the urgument
    def __init__(self,):
       
        Book.total_books += 1
#implementing the class method to display  totla number of books created
    @classmethod
    def display_total_books(cls):
        print(f"The number of books entered is {cls.total_books}")

#creatint the instance of oue class and calling it
book1 = Book()
Book.display_total_books()        




