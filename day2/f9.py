def checkPrime(n):
    i=1
    count=0
    while(i<=n):
        if(n%i==0):
            count+=1
        i=i+1
    if (count==2):
        print(" a prime number")
    else:
        print(" not Prime Number")
x=int(input("Enter the number"))
checkPrime(x)