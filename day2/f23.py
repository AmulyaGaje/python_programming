def Perfect(n):
    for i in range(1,n+1):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j
        if(sum==i):
            print(i)
x=int(input())
Perfect(x)