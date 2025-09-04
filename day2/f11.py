def SumOfDigits(n):
    rem=0
    while(n>0):
        sum=n%10
        rem=rem+sum
        n=n//10
    return rem
x=int(input("ENter a number"))
print(SumOfDigits(x))