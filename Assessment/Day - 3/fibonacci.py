# Getting terms input from user
num = int(input("Enter the number of terms:"))

# fibonacci recursive function
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

# values finding based on range   
for i in range(0,num):
    result = fibonacci(i)
    print(result,end=" ")