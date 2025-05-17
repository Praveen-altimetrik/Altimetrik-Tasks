# id,name,course,average marks
#4 methods add, view, update, delete

# Creating a class Student
class Student: 

    def __init__(self, student_id_no, name, course): 

        self.student_id_no = student_id_no 
        self.name = name 
        self.course = course 

    def __str__(self): 
        return f"student_id No: {self.student_id_no}, Name: {self.name}, Course: {self.course}" 


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

        with open("demo.txt",'a') as file:
            file.write(content)
        print("Process Completed...")


    def view_record(self): 
        
        for id, info in self.container.items():
            print(f"ID: {id}, Name: {info['name']}, Course: {info['course']}, Average_marks: {info['average_marks']}")
        if not self.container:
            print(f"Record not found {id}")

    def update_student(self, student_id_no, name=None, course=None): 
        if student_id_no in self.container: 
            if name: 
                self.container[student_id_no].name = name 
            if course: 
                self.container[student_id_no].course = course 
            print(" Student updated.") 
        else: 
            print(" Student not found.") 

    def delete_student(self, student_id_no): 
        if student_id_no in self.container: 
            del self.container[student_id_no] 
            print(" Student deleted.") 
        else: 
            print(" Student not found.") 

obj = StudentRecords() 

while True: 

        print("\n--- Student Records ---") 
        print("1. Add Student") 
        print("2. View All Students") 
        print("3. Update Student") 
        print("4. Delete Student") 
        print("5. Exit") 

        choice = input("Enter your choice (1-5): ") 

        if choice == '1': 
            obj.add_student()

        elif choice == '2': 
            obj.view_record() 

        elif choice == '3': 
            student_id = input("Enter student_id to update: ") 
            name = input("Enter the name to update: ") 
            course = input("Enter the course to update: ") 
            obj.update_student(student_id, name or None, course or None) 

        elif choice == '4': 
            student_id = input("Enter student_id No to delete: ") 
            obj.delete_student(student_id) 

        elif choice == '5': 
            print("Exited Successfully...") 
            break 

        else: 
            print(" Invalid choice.Please enter from 1-5..") 