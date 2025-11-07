#fibnacci series
def fib(n):
    if n<=1:
        return n
    else :
        return fib(n-1)+fib(n-2)
    
n=int(input("Enter a number to find fibonacci series: "))
for i in range(n):
    print(fib(i),end=" ")
    