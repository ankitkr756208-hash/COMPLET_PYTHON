n=int(input("Enter the no:"))
r=0
x=n
while n>0 :
    d=n%10
    r=r*10+d
    n=n//10
    print("the reverse no:",r)
    if x==r:
        print("pallidrome",x)
    else:
        print("not a pallidrome no")    