# n=int (input("Enter the integer :"))
# x=n
# rev=0
# while n>0:
#     n=n%10
#     rev=rev*10 +n
#     n =n//10
# print("The reverse of",x,"is",rev)

n = int(input("Enter the integer: "))
count = len(str(n))
t = n

sum = 0
while n > 0:
    digit = n % 10           # Get last digit
    sum = digit + t ** count
    n = n // 10              # Remove last digit

if sum == t:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")


