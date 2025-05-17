class College:
    
    University = "Anna University" # class variable
    # Constructor
    def __init__(self,id,name,dept,place):
        self.student_id = id
        self.student_name = name
        self.stuent_dept = dept
        self.place = place
    

    # Method to display product details

    def display(self):
        print("University:{}".format(College.University))
        print("Student_id: {}".format(self.student_id))
        print("Student_name: {}".format(self.student_name))
        print("Student_department: {}".format(self.stuent_dept))
        print("Location: {}".format(self.place))

    # main function

def main():
    print("Student information...")

    #creating object

    p1 = College(1,"praveen","cse","villupuram")
    p2 = College(2,"arun","eee","madurai")

    p1.display()
    p2.display()

    # entry point

if __name__ == "__main__":
    main()        