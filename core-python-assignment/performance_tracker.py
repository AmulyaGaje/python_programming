def calculate_average(m):
    sum=0
    for i in m:
        sum+=i
    return sum/len(m)
n=int(input("Enter the number of students"))
s={}
top=0
top_per=""
for i in range(n):
    name=input(f"Enter the name of student {i+1}")
    marks=list(map(int,input("Enter the marks").split()))
    avg=calculate_average(marks)
    s[name]=avg
    if avg>top:
        top=avg
        top_per=name
print("Average Marks=",s)
print("Top Performer:",top_per)