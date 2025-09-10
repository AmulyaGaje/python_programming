#displaying negative numbers
def Display(n):
    li=[]
    for i in n:
        if(i<0):
            li.append(i)
    print(li)
l1=map(int,input("Enter eleemnts in a list").split())
Display(l1)