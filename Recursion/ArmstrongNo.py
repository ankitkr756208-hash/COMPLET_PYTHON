num=int(input("Enter a number to check Armstrong or not: "))
sum=0
temp=num
n=len(str(num))

while temp>0:
    rem=temp % 10
    sum+=rem ** n
    temp//=10


if sum==num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

