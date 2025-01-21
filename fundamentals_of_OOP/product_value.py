#Exercise 2: Creating a Product Catalog
#Instruction:
#Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the
#  total value of products in stock.

#creating the class
class products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
#creating the instance of a class
product = products("maxi_skirts", 750,20)

#calling the method and displaying the total value
print(product.total_value())
