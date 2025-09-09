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
print("positive feedback= ",m,"%")