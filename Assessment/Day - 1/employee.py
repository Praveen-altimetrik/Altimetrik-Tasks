#Getting emoployee data based on parameters

emoployee_id = int(input("Enter the employee id:"))
employee_name = input("Enter the employee name:")
emoployee_job = input("Enter the employee job:")
employee_basicpay = int(input("Enter the basicpay:"))

# Providing allowance based on job position

allowance = employee_basicpay * (0.05 if emoployee_job == "manager" else 0.08 if emoployee_job == "developer" else 0.10 if emoployee_job == "analyst" else 0)

# Calculating payable salary

payable_salary = employee_basicpay + allowance

#print statement for adding space between getting values and displaying result
print()

# Displaying employee credentials along with allowance 
print("Employee name: {}, Employee id:{}, Employee Allowance:{}".format(employee_name,emoployee_id,payable_salary))


