<<<<<<< HEAD
def Feedback(x):
    count=0
    l=len(x)
    for i in x:
        if(i==4 or i==5):
            count+=1
    per=(count/l)*100
    return per
item=input("ratings =")
li=list(map(int,item.split()))
m=Feedback(li)
=======
def Feedback(x):
    count=0
    l=len(x)
    for i in x:
        if(i==4 or i==5):
            count+=1
    per=(count/l)*100
    return per
item=input("ratings =")
li=list(map(int,item.split()))
m=Feedback(li)
>>>>>>> 0fa6456496e9d71ee8c18890d9747d5bd6d029d0
print("positive feedback= ",m,"%")