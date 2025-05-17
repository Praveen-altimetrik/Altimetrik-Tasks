# default argument : default value will be passed if argument not passed by the user

def add(x,y=1):
    return x+y

print(add(2,4))
print(add(2))