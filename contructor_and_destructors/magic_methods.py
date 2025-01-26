class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_book(self):
        '''print(f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}")'''

    def __str__(self):
        return f"The mystic {self.author} wrote '{self.title}' book which has {self.pages} pages"

# Creating an instance of the class
book = Books("Inner Engineering", "Sadhguru", 257)

# Calling the instance method
book.display_book()

# Printing the formatted string representation
print(book)
