x=input("Enter a string")
y=input("Enter other string")
def Length(x):
    count=0
    for i in x:
        count+=1
    print(count)
def Compare(x,y):
    if(x==y):
        print("Equal")
    else:
        print("Not Equal")
def Concat(x,y):
    z=x+y
    print(z)
Length(x)
Compare(x,y)
Concat(x,y)