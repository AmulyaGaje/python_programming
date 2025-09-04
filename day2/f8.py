def factorial(n):
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i=i+1
    return fact
x=int(input("Enter a number"))
print(f"The factorial of {x} is {factorial(x)}")