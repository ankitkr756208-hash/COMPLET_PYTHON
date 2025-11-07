try:
    a =int(input("Enter the number:"))
    print(a)


except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
except Exception as e:
    print("Invalid Input",e)

print("Program continues...")

