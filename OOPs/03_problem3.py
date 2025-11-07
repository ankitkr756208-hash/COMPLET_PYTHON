class demo:
    a=4

o=demo()
print(o.a)# print the class attribute because instance attribute is not present
o.a=0 # Instance attributate is set
print(o.a)#Print the instance attribute because instance attributive is present
print(demo.a)#Print the class attribute because instance attribute is not present in class