


a = {1:"hello",5:"you",2:"praveen",3:"how",4:"are"}
b = dict(sorted(a.items(),key=lambda item:item[0]))

print(b)

a = {1:"hello",5:"you",2:"praveen",3:"how",4:"are"}
b = dict(filter(lambda item:item[0]>1,a.items()))
c = b
print(dict(sorted(c.items(),key=lambda item:item[0])))
print(c)

