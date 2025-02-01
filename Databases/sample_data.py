import mysql.connector

# Function to establish a database connection
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Moha@22nov",
        database="LibraryManagementSystem"  # Using the correct database
    )
    return conn

conn = connect_db()
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS LibraryManagementSystem")

# Use the database (this makes sure we're working within the correct database)
cursor.execute("USE LibraryManagementSystem")

# Create the books table (this is your SQL query)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,    
        title VARCHAR(255),                   
        author VARCHAR(255),                  
        isbn VARCHAR(255)                     
    )
""")

# Commit changes to the database
conn.commit()

# Checking if the connection is successful
if conn.is_connected():
    print("Connected successfully and table created!")
cursor.close()
conn.close()




# Add a new book
def add_book(title, author, isbn):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, isbn))

    conn.commit()
    print(f"Book '{title}' added successfully!")

    cursor.close()
    conn.close()

# Search for a book by title
def search_book(title):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, ("%" + title + "%",))

    books = cursor.fetchall()
    if books:
        print("Books found:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print("No books found with that title.")

    cursor.close()
    conn.close()

# List all books in the library
def list_books():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM books"
    cursor.execute(query)

    books = cursor.fetchall()
    if books:
        print("All books in the library:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print("No books available in the library.")

    cursor.close()
    conn.close()

# Bonus: Delete a book by ID
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))

    conn.commit()
    print(f"Book with ID {book_id} deleted successfully!")

    cursor.close()
    conn.close()

# Main menu for the user to choose actions
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Search for a book by title")
        print("3. List all books")
        print("4. Delete a book by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            add_book(title, author, isbn)

        elif choice == "2":
            title = input("Enter the title to search for: ")
            search_book(title)

        elif choice == "3":
            list_books()

        elif choice == "4":
            book_id = int(input("Enter the ID of the book to delete: "))
            delete_book(book_id)

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()