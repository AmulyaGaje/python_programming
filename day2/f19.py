def checkPrime(n):
    for j in range(1,n+1):
        i=1
        count=0
        while(i<=j):
            if(j%i==0):
                count+=1
            i=i+1
        if (count==2):
            print(j)
x=int(input("Enter the number"))
print("The NO OF PRIMES TILL ",x)
checkPrime(x)