#Exercise 2: File Handling with FileNotFoundError

#Instructions:

#Write a program that attempts to open and read data from a file specified by the user.
#Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.


def read_file():
    # Prompt user to enter the file name
    file_name = input("Enter the name of the file to read (including the extension): ")
    
    try:
        # Attempt to open and read the file
        with open(file_name, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"\nError: The file '{file_name}' does not exist. Please check the file name and try again.")
   
if __name__ == "__main__":
    read_file()
