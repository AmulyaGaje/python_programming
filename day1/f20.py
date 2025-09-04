def largest(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
a,b,c=map(int,input("Enter the three numbers").split())
res=largest(a,b,c)
print(f"{res} is largest")
