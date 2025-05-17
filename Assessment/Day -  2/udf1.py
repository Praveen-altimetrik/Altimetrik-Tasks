# write a UDF to find the given number is perfect number or not

def perfect_number(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False
    
# main function
    
if __name__ == "__main__":
    num = int(input("Enter a number:"))
    if perfect_number(num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

print(__name__)