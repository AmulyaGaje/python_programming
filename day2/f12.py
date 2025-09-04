def count(n):
    count=0
    while(n>0):
        n=n//10
        count=count+1
    return count
x=int(input("Enter a number"))
print(count(x))
