def Factors(n):
    for i in range(1,n):
        if(n%i==0):
            w=1
            count=0
            while(w<=i):
                if(i%w==0):
                    count+=1
                w=w+1
            if (count==2):
                print(i)
x=int(input())
Factors(x)