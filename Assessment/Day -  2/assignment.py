# Function to find whether given number is even or not

# Getting user input
num = int(input("Enter the number:"))

# Defining is_even function
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

# Returned output is stored in variable and printed
output = is_even(num)
print("Whether {} is even or not True || False: {}".format(num,output))


# Function to find area of circle

# Getting radius input from user
radius = int(input("Enter the radius:"))

# Defining function to find area of the circle
def area_of_circle(radius):
    area = 3.14*radius**2
    return area

# Returned value is stored in variable and printed
output = area_of_circle(radius)
print(f"The area of the circle is:{output}")
