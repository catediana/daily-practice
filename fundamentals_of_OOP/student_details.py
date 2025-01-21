#Exercise 1: Creating a Student Class

#Instructions:

#Define a Student class with attributes like name and age. Include a method to display student information.
class students :
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def student_details(self):
        print(f"name: {self.name}, age: {self.age}")
student = students("cate", 23)
student.student_details()