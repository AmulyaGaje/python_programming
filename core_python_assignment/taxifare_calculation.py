<<<<<<< HEAD
def caclculate_fare(li):
    sum=0
    total=0
    for i in li:
        x=(i*10)+50
        print(f"Trip{i+1}:${x}")
        sum=sum+x
    return sum
x=input("trips=")
li=map(int,x.split())
res=caclculate_fare(li)
=======
def caclculate_fare(li):
    sum=0
    total=0
    for i in li:
        x=(i*10)+50
        print(f"Trip{i+1}:${x}")
        sum=sum+x
    return sum
x=input("trips=")
li=map(int,x.split())
res=caclculate_fare(li)
>>>>>>> 0fa6456496e9d71ee8c18890d9747d5bd6d029d0
print("Total Fare :$",res)