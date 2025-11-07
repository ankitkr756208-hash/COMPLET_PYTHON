def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)
n = int(input("Enter a number to find sum of natural numbers: "))
print(f"The sum of first {n} natural numbers is: {sum_n(n)}")