# Creating Student class (Base class)
class Student:

    # Constructor
    def __init__(self,id,name):
        self.id = id
        self.name = name

    # Method 1
    def display(self):
        print("Id:{}, Name of the student is:{}".format(self.id,self.name))

# Creating College class (Derived class)
class College(Student):

    # Constructor of derived class
    def __init__(self,id,name,dept,college):
        super().__init__(id,name) # Accessing members of base class
        self.department = dept
        self.college = college

    # Method 1
    def display(self):
        print("ID:{}, Name:{}, Department:{}, College:{}".format(self.id,self.name,self.department,self.college))

# Main function
def main():
    obj1 = College(1,"praveen","CSE","IFET")
    obj2 = College(2,"koushik","MECH","RGUKT")
    obj3 = Student(3,"Arun")

    obj1.display()
    obj2.display()
    obj3.display()

# Invoking main function
if __name__ == "__main__":
    main()



        
