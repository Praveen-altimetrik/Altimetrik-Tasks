#Getting salesman id and salesman value as user input

salesman_id = int(input())
salesman_value = int(input())

# Finding Commmission

if salesman_value <= 10000:
    commission = 0
elif salesman_value > 10001 and salesman_value < 50000:
    commission = salesman_value*0.1
elif salesman_value > 50001 and salesman_value < 100000:
    commission = salesman_value*0.15
elif salesman_value > 100000:
    commission = salesman_value*0.20

#Printing salesman_id with Commission

print(f"salesman_id:{salesman_id},Commission:{commission}")