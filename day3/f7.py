def Unique(li):

    l = len(li)
    x=[]  
    for i in range(l): 
        count=0
        for j in range(l):
            if li[i] == li[j]:
               count+=1
        if count==1:
            x.append(li[i])
    print(x)
li = list(map(int, input("Enter elements: ").split()))
Unique(li)
