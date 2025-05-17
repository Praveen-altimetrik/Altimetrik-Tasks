# Content displayed to user to select a choice

print("Welcome to file handling....")
print("1. Write a file")
print("2. Read a file")
print("3. Append a file")
print("4. Exit")

# Function to write content in a file

def write_in_file():

    # Exception handling while writing in file
    try:
        filename = input("Enter the filename:")
        content = input("Enter the content to write in the file:")
        with open(filename,'w') as file:
                file.write(content)
        print("File written successfully..")
    except FileNotFoundError:
        print("Error: File not Found")

# Function to read content in a file

def read_a_file():

    # Exception handling while reading in file
    try:
        filename = input("Enter the filename to read:")
        with open(filename,'r') as file:
            content = file.read()
            print("The content present in the file is: {}".format(content))
            print("File read successfully..")
    except FileNotFoundError:
        print("Error: File not Found")
    except Exception as e:
        print("Error in reading the file",e)

# Function to append content in a file

def append_in_file():

    # Exception handling while appending in file
    try:
        filename = input("Enter the filename to append:")
        content = input("Enter the content to append in file:")
        with open(filename,'a') as file:
            file.write(content)
        print("Content appended successfully..")
    except FileNotFoundError:
        print("Error: File not Found")
    except Exception as exception:
        print("Error Found:",exception)

# main function

def main():
    while True:
        choice = int(input("Enter your choice from (1-4): "))
        if choice == 1:
            write_in_file()
        if choice == 2:
            read_a_file()
        if choice == 3:
            append_in_file()
        if choice == 4:
            print("Exit Successfully..")
            break

if __name__ == "__main__":
    main()

