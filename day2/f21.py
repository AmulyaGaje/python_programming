def armstrong(j):
    for n in range(1,j):
        rev=0
        m=str(n)
        l=len(m)
        temp=n
        while(n>0):
            r=n%10
            rev=rev+r**l
            n=n//10
        if(temp==rev):
            print(temp)
n=int(input())
armstrong(n)