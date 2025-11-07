n=int(input("enter limit:"))
m={}
mob=0
name=""
i=0
for i in range(0,n):
    mob=int(input("Enter mobile no:"))
    name=str(input("Enter name:"))
    z2=dict({mob:name})
    m.update(z2)
print(m)
n=int(input("Enter the no of search in dictionary:"))
print("The no of person is",m[n])    
