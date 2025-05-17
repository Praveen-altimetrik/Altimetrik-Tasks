with open('employees.txt','w') as file:
    file.write("ID,Name,Department,Salary\n")
    file.write("101,John Doe,IT,60000\n")
    file.write("102,Jane Smith,HR,55000\n")
    file.write("103,Emily Johnson,Finance,70000\n")

# Step 2: Reading Data from a file
# Reading employee data

try:
    with open('employees.txt','r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")

# Step 3: Appending Data to a File
# Adding new employee data

with open('employees.txt','a') as file:
    file.write("104,Michael Brown,Marketing,62000\n")

print("New employee added successfully")

# Step 4: Handling Exception in File Handling

try:
    with open('nonexistent_file.txt','r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist")