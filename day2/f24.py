def Factors(n):
    for i in range(1,n):
        if(n%i==0):
            print(i)
x=int(input())
Factors(x)
