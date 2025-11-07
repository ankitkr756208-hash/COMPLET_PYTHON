def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
    
n1=int(input("Enter the number n1: "))
n2=int(input("Enter the number n2: "))

print(f"The GCD of {n1} and {n2} is : {hcf(n1,n2)}")