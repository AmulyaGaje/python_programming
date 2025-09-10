<<<<<<< HEAD
def priceCalculation(li):
    price=0
    if(len(li)==0):
        price=0
    elif(len(li)>0 and len(li)<6):
        for x in li.values():
            price+=x
    else:
        sum=0
        for x in li.values():
            sum+=x
        price=sum-(0.1*sum)
    return price
n=int(input("Enter the no. of items"))
li={}
for i in range(1,n+1):
    key=input(f"Enter the item name {i}")
    value=float(input("Enter the price "))
    li[key]=value
total=priceCalculation(li)
=======
def priceCalculation(li):
    price=0
    if(len(li)==0):
        price=0
    elif(len(li)>0 and len(li)<6):
        for x in li.values():
            price+=x
    else:
        sum=0
        for x in li.values():
            sum+=x
        price=sum-(0.1*sum)
    return price
n=int(input("Enter the no. of items"))
li={}
for i in range(1,n+1):
    key=input(f"Enter the item name {i}")
    value=float(input("Enter the price "))
    li[key]=value
total=priceCalculation(li)
>>>>>>> 0fa6456496e9d71ee8c18890d9747d5bd6d029d0
print("Total Price :",total)