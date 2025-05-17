# Creating class Student
class Student: 

    def __init__(self, student_no, name, course,average_marks): 
        self.student_no = student_no 
        self.name = name 
        self.course = course 
        self.average_marks = average_marks

    def __str__(self): 
        return f"Roll No: {self.student_no}, Name: {self.name}, Course: {self.course}, Average_marks: {self.average_marks}" 

# Class Student Records
class StudentRecords: 

    def __init__(self): 
        self.container = {}  

    def add_student(self): 
         student_id = int(input("Emter the id:"))
         if student_id in self.container:
            print("Student Id already exists.")
         else:
            name = input("Enter the name:")
            course = input("Enter the course:")
            average_marks = float(input("Enter the average marks:"))
            self.container.update({student_id :{
            'name': name,
            'course': course,
            'average_marks':average_marks         
        }})
         for student_id, info in self.container.items():
            content = f"ID: {student_id}, Name: {info['name']}, Course: {info['course']}, Average_marks: {info['average_marks']}\n"

         with open("test.txt",'a') as file:
            file.write(content)
         print("Process Completed...")

 
    # Function to view records
    def view_records(self): 

        for id, info in self.container.items():
            print("...Students Record...")
            print(f"ID: {id}, Name: {info['name']}, Course: {info['course']}, Average_marks: {info['average_marks']}")
        if not self.container:
            print(f"Record not found")

    # Update Function
    def update_student(self): 
        if not self.container:
            print("No records in database...")
            return
        student_id = int(input("Enter Roll No to update: "))
        new_name = input("Enter new name: ") 
        new_course = input("Enter new course: ") 
        new_average_marks = float(input("Enter the average_marks :"))
        if new_name: 
            self.container[student_id]["name"] = new_name 
        if new_course: 
            self.container[student_id]["course"] = new_course 
        if new_average_marks:
            try:
                self.container[student_id]["average_marks"] = float(new_average_marks)
            except ValueError:
                print("Invalid marks. keeping old value..")
            print(" Student updated.") 
        else: 
            print(" Student not found.") 

 
    # Delete Function
    def delete_student(self, student_no): 

        remove = self.container.pop(student_no)
        if remove:
            print("Students deleted")
        else:
            print("Student not found")


# Main function
def main(): 

    # Creation of Object
    obj = StudentRecords() 

 

    while True: 
        # Choice Selection
        print("\n--- Student Record Management ---") 
        print("1. Add Student") 
        print("2. View All container") 
        print("3. Update Student") 
        print("4. Delete Student") 
        print("5. Exit") 

        choice = input("Enter choice (1-5): ") 

        if choice == '1': 
            obj.add_student() 

        elif choice == '2': 
            obj.view_records() 

        elif choice == '3': 
            obj.update_student() 

        elif choice == '4': 
            roll = int(input("Enter Roll No to delete: "))
            obj.delete_student(roll) 

        elif choice == '5': 
            print("Exiting the Record System...") 
            break 
        
        else: 
            print(" Invalid choice. Please enter values from (1-5)") 

# Main function
if __name__ == "__main__":
    main()