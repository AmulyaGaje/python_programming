def count(x):
    ec=0
    oc=0
    for i in x:
        if(i%2==0):
            ec+=1
        else:
            oc+=1
    print("Even numbers count=",ec)
    print("Odd numbers count =",oc)
x=map(int,input("Enter numbers in alist").split())
count(x)
