a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))
d=float(input("Enter fourth number: "))
if a>b and a>c and a>d:
    print(a,"is the gratest NO.")
elif b>a and b>c and b>d:
    print(b,"is the gratest NO.")
elif c>a and c>b and c>d:
    print(c,"is the gratest NO.")
else:
    print(d,"is the gratest NO.")