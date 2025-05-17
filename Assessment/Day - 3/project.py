# id,name,course,average marks
#4 methods add, view, update, delete

# Creating a class Student
class Student:

    # Constructor
    def __init__(self):
        self.container = {}

    # Add operation
    def add_op(self):
        id = int(input("Emter the id:"))
        if id in self.container:
            print("Student Id already exists.")
        else:
            name = input("Enter the name:")
            course = input("Enter the course:")
            average_marks = float(input("Enter the average marks:"))
            self.container.update({id :{
            'name': name,
            'course': course,
            'average_marks':average_marks         
        }})
        for id, info in self.container.items():
            content = f"ID: {id}, Name: {info['name']}, Course: {info['course']}, Average_marks: {info['average_marks']}\n"

        with open("demo.txt",'a') as file:
            file.write(content)
        print("Process Completed...")

    #Dunder method
    def __str__(self):
        return f"the id is: {self.id} and the name is: {self.name}"

    # View method
    def view(self):
       if not self.container:
            print(f"Record not found {id}")
       for id, info in self.container.items():
            print(f"ID: {id}, Name: {info['name']}, Course: {info['course']}, Average_marks: {info['average_marks']}")
       

    def update(self,change):
        if id not in self.container:
            name = input("Enter the name:")
            course = input("Enter the course:")
            average_marks = float(input("Enter the average marks:"))
            self.container[change] = {"Name":name,"course":course,"Average_marks":average_marks}
        
        else:
            print("Enter valid id")



    # Delete method
    def delete(self,search_id):
        if not self.container:
            print("No records to delete...")
        if search_id in self.container:
            del self.container[search_id]
            print("Id deleted sucessfully..")
        else:
            print(f"{search_id} not present")

obj = Student()

while True:
    print("Select option to perform operation -> (1-5):")
    print("1. ADD")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        obj.add_op()
    if choice == 2:
        obj.view()
    if choice == 3:
        change = int(input("Enter the id:"))
        obj.update(change)
    if choice == 4:
        search_id = input("Enter the id to delete:")
        obj.delete(search_id)
    if choice == 5:
        print("Exiting the program")
        break
    




        