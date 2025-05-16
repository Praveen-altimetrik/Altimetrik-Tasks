# Getting user input for student id, 3 subject marks

student_id = int(input("Enter the student ID:"))

maths = int(input("Enter the maths mark:"))
science = int(input("Enter the science mark:"))
english = int(input("Enter the english mark:"))

# Checking Result
average = maths+science+english/3

if maths and science and english >= 40:
    result = "Pass"
    if average>=80:
        grade = "A+"
    elif average>60 and average <79:
        grade = "A"
    elif average > 40 and average <59:
        grade = "B" 
else:
    result = "Fail"
    grade = "Grade needs improvement"

print("Student ID:{}, Result:{}, Average:{}, Grade:{}".format(student_id,result,average,grade))