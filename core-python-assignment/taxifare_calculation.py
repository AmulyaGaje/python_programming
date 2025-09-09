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
print("Total Fare :$",res)