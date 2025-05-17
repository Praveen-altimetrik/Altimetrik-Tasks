# Duck typing is a concept in programming where the type or class of an object is determined by the methods and properities that the object has, 
# rather than the actual type of the object itself

class IT:

    def service(self):
        print("Focus on developing the software..")

class HR:

    def service(self):
        print("Focus on selecting the candidate..")

class IT_Support:

    def service(self):
        print("Focus on feedback and respond to users..")

def select(option):
    option.service()

choice = input("Enter the choice:")
if choice == "IT":
    select(IT())
if choice == "HR":
    select(HR())
if choice == "IT_SUPPORT":
    select(IT_Support())