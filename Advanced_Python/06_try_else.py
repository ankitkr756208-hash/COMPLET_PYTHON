try:
    a=int(input("Enter the number:"))
    print(a)

except Exception as e:
    print(e)

else:
    print("No exception occurred. The input number is:", a)