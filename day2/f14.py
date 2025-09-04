def find(x):
    temp=x%10
    while(x>0):
        n=x%10
        x=x//10
    print("Sum=",n+temp)
m=int(input())
find(m)
