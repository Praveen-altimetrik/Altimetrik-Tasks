# Variable length argument

def total(*marks):
    print(sum(marks))

total(10,20,30)

# Multiple Keyword varaible length argument

def show_profile(**info):
    for key,value in info.items():
        print(f"{key}:{value}",end=" ")

show_profile(name = "praveen", age = 22, location = "villupuram")