def SecondLargest(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i]<li[j]):
                temp=li[i]
                li[i]=li[j]
                li[j]=temp
    print("tHE SECOND LARGEST NUMBER IS",li[1])
li=input("Enter the elements").split()
SecondLargest(li)


