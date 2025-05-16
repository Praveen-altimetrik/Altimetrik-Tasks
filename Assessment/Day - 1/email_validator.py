#Employee data

employees = [
    {"name":" Alice Johnson","email":"Alice.j@company.com"},
    {"name": "harry","email":"harry@comp.com"},
    {"name": "Carol Lee", "email":"carol.lee@otherdomain.com"}
]

#Python code with string Methods:




for emp in employees:
    name = emp["name"].strip() # Removes Extra Spaces
    email = emp["email"].strip().lower() # Removes spaces and converts into lower case

    # Validating the email

    if not email.startswith(name[0].lower()):
        print(f" Invalid email format for {name} -  does not start with name")
        continue


    if "@company.com" not in email:
        print(f" Invalid domain for {name}:{email}")
        continue
        
    
    #Generate username

    parts = name.lower().split()
    if len(parts) >= 2:
        username = parts[0] + "." + parts[1]
    else:
        username = parts[0]

#Output result
print()
print(f"Name:{name} | Email:{email} | username:{username}")
