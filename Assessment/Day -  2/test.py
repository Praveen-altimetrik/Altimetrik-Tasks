# Function to find number of words in a string

#defining function
def no_of_words(string):
    spliting = string.split()
    return len(spliting)

#calling the function with parameter
result = no_of_words("praveen is in altimetrik")
print(f"Number of words in the string is:{result}")

def calculate_bill(price,quantity,discount=0):
    total = price*quantity
    final_amount = total - (total*discount/100)
    return final_amount

output = calculate_bill(1000,2)
print(output)


