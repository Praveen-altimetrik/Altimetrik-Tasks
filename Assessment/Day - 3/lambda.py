add = lambda x, y: x+y

print(add(1,2))

employees = [
    {"name":"Smith", "salary": 50000},
    {"name":"Allen", "salary": 60000},
    {"name":"James", "salary": 45000},
]

# Sort employeses by salary using lambda

sorted_employees = sorted(employees, key = lambda x: x["salary"])

for emp in sorted_employees:
    print(emp)