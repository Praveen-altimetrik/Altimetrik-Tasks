# csv file handling in python

# reading and writing list data to a CSV file

## **1. Writing to a CSV file

import csv

data = [
    ["Name","Age","Grade"],
    ["Alice",20,"A"],
    ["Bob",22,"B"],
    ["Charlie",21,"A"]
]

with open('studentdata.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# read the csv file

with open('studentdata.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

