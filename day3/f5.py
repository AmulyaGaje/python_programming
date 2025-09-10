def Remove(li,x):
    li1=[]
    for i in range(len(li)):
        if i!=x:
            li1.append(li[i])
    print(li1)
li=list(map(int,input("Enter elements").split()))
x=int(input("Enter the position"))
Remove(li,x)

