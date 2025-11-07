def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    

a=int(input("Enter the no:"))
b=int(input("Enter the no:"))
c=int(input("Enter the no:"))
print(greatest(a,b,c))
