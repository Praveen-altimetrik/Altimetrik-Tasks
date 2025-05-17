# lambda function to find greatest of three numbers
# we can also use max function

f = lambda a,b,c : a if a>b and a>c else b if b>a and b>c else c
print(f(50,70,100))

