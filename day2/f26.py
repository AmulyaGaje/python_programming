def Fibonacci(x):
    for n in range(1,x+1):
        if(n==1):
            return n
        else:
            return (n-1)+(n-2)
x=int(input())
print(Fibonacci(x))
