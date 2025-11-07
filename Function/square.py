def square(a,b=3):
    return  a**2,b**2
print(square(2))
print(square(24,5))

# Variable Scope Example

x = 10  # Global variable

def outer():
    y = 20  # Enclosing variable

    def inner():
        z = 30  # Local variable
        print("Local:", z)
        print("Enclosing:", y)
        print("Global:", x)
    
    inner()

outer()
