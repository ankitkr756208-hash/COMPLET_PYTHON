def sum(a,b):
    return a +b,a-b,a*b,a/b,a%b,a**b

print(sum(2,3))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))
print(fact(6))


print("chack even odd number")
def  is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(4))


print("Average Number")
def avg(n1,n2,n3):
    return (n1 +n2+n3)/3
print(avg(2,3,4))


