class Employee:

    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"The name of the employee is: {self.name} and the role is: {self.role}"
    

    
    def __add__(self,incentives):
        return self.salary+incentives.salary
    
obj1 = Employee("Praveen","Intern",10000)
obj2 = Employee("Koushik","intern",10000)

print(obj1)
print(obj2)
print(obj1+obj2)