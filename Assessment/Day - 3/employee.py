class Employee:
    company_name = "Southern Infotech Pvt Ltd"
    def __init__(self,name,emp_id,department,salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Company: {Employee.company_name}")
        print(f"Name: {self.name}")
        print(f"Emp ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: Rs{self.salary}")
        print("-" * 30)

# Method with return type and no parameter
    def annual_salary(self):
        return self.salary * 12

# Method without return type and with parameter
    def apply_increment(self, percentage):
        increment = self.salary * (percentage / 100)
        self.salary += increment

# Method with return type and with no parameter
    def is_high_earner(self):
        return self.salary > 70000
    
    @staticmethod
    def welcome_message():
        print("Welcome to Southern Infotech Pvt Ltd...")


# Creating employee objects

emp1 = Employee("Ravikumar","EMP101","HR",80000)
emp2 = Employee("Rithik","EMP102","IT",90000)
emp3 = Employee("Lakshmi Priya","EMP103","Support-Team",18000)

def main():

    emp1.display_details()  


if __name__ == "__main__":
    main()