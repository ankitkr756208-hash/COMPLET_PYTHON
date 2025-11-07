first=int(input("Enter first no:"))
operator=input("enter operator(+,-,*,//,/,%):")
second=int(input("Enter the second no:"))

if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="//":
    print(first//second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("invalid operations")
